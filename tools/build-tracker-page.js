// Build docs/index.html (the GitHub Pages tracker) from TRACKING.md + design/screens.json.
// TRACKING.md is the only source of truth for status; screens.json only adds per-screen detail.
// Usage (from the repo root):  node tools/build-tracker-page.js
const fs = require('fs');
const path = require('path');
const root = path.join(__dirname, '..');
const md = fs.readFileSync(path.join(root, 'TRACKING.md'), 'utf8');
let plan = { screens: [], phases: [], decisions: [] };
try { plan = JSON.parse(fs.readFileSync(path.join(root, 'design', 'screens.json'), 'utf8')); } catch (e) { /* detail is optional */ }
const detail = Object.fromEntries((plan.screens || []).map((s) => [s.id, s]));
const phaseInfo = Object.fromEntries((plan.phases || []).map((p) => [p.id, p]));
const decInfo = Object.fromEntries((plan.decisions || []).map((d) => [d.id, d]));

const esc = (s) => String(s == null ? '' : s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const inline = (s) => esc(s).replace(/`([^`]+)`/g, '<code>$1</code>').replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>');

// ---- parse TRACKING.md ----
const STATES = ['Chưa làm', 'Đang thiết kế', 'Đã thiết kế', 'Đang code', 'Xong'];
const KEY = { 'Chưa làm': 'todo', 'Đang thiết kế': 'designing', 'Đã thiết kế': 'designed', 'Đang code': 'building', 'Xong': 'done' };
const flows = []; const phases = []; const decisions = []; const log = [];
let section = ''; let flow = null;
for (const line of md.split('\n')) {
  if (line.startsWith('## ')) { section = line.slice(3).trim(); continue; }
  if (line.startsWith('### ') && section.startsWith('Màn hình')) { flow = { name: line.slice(4).trim(), rows: [] }; flows.push(flow); continue; }
  if (section.startsWith('Nhật ký') && line.startsWith('- ')) { log.push(line.slice(2)); continue; }
  if (!line.startsWith('|') || line.startsWith('|---') || line.startsWith('| Mã')) continue;
  const c = line.split('|').slice(1, -1).map((s) => s.trim());
  if (section.startsWith('Màn hình') && flow) flow.rows.push({ id: c[0], name: c[1], pri: c[2], st: STATES.includes(c[3]) ? c[3] : 'Chưa làm', note: c[4] || '' });
  else if (section.startsWith('Lộ trình')) phases.push({ id: c[0], name: c[1], effort: c[2], st: c[3] });
  else if (section.startsWith('Quyết định')) decisions.push({ id: c[0], q: c[1], rec: c[2], chosen: c[3] });
}
const screens = flows.flatMap((f) => f.rows);
const mvp = screens.filter((s) => s.pri === 'Bản đầu');
const isDesigned = (s) => ['Đã thiết kế', 'Đang code', 'Xong'].includes(s.st);
const pct = (a, b) => (b ? Math.round((a / b) * 100) : 0);
const nDesigned = mvp.filter(isDesigned).length;
const nDone = mvp.filter((s) => s.st === 'Xong').length;
const nDecided = decisions.filter((d) => d.chosen).length;
const nPhaseDone = phases.filter((p) => p.st === 'Xong').length;
const curPhase = phases.find((p) => p.st !== 'Xong');
const counts = Object.fromEntries(STATES.map((s) => [s, screens.filter((x) => x.st === s).length]));
const updated = new Date().toLocaleString('vi-VN', { timeZone: 'Asia/Ho_Chi_Minh', hour: '2-digit', minute: '2-digit', day: '2-digit', month: '2-digit', year: 'numeric' });

const list = (a) => (a && a.length ? `<ul>${a.map((x) => `<li>${esc(x)}</li>`).join('')}</ul>` : '');
const screenRow = (s) => {
  const d = detail[s.id] || {};
  const body = [
    d.purpose_vi && `<p class="pur">${esc(d.purpose_vi)}</p>`,
    d.content_vi && `<h5>Nội dung</h5>${list(d.content_vi)}`,
    d.states_vi && `<h5>Trạng thái con</h5>${list(d.states_vi)}`,
    (d.entry_vi || d.exit_vi) && `<h5>Đi từ đâu, tới đâu</h5><p>${esc(d.entry_vi)}</p><p>${esc(d.exit_vi)}</p>`,
    d.via_moment_vi && `<h5>Vía làm gì</h5><p>${esc(d.via_moment_vi)}</p>`,
    d.art_needed_vi && `<h5>Hình cần render</h5><p>${esc(d.art_needed_vi)}</p>`,
    d.notes_vi && `<h5>Ghi chú kế hoạch</h5><p>${esc(d.notes_vi)}</p>`,
  ].filter(Boolean).join('');
  const k = KEY[s.st];
  return `<details class="row ${k}"><summary><span class="chk" aria-hidden="true"></span><span class="rid">${esc(s.id)}</span><span class="rn">${esc(s.name)}${s.note ? `<small>${inline(s.note)}</small>` : ''}</span><span class="tags">${s.pri !== 'Bản đầu' ? `<span class="tg">${esc(s.pri)}</span>` : ''}<span class="pill ${k}">${esc(s.st)}</span></span></summary>${body ? `<div class="det">${body}</div>` : ''}</details>`;
};
const flowCard = (f) => {
  const d = f.rows.filter(isDesigned).length;
  const c = f.rows.filter((s) => s.st === 'Xong').length;
  const active = f.rows.some((s) => ['Đang thiết kế', 'Đang code'].includes(s.st));
  return `<section class="card flow"><header><h3>${esc(f.name)}${active ? ' <span class="badge">ĐANG LÀM</span>' : ''}</h3><span class="mono">${d}/${f.rows.length} thiết kế · ${c} xong</span></header><div class="mini"><i style="width:${pct(d, f.rows.length)}%"></i></div>${f.rows.map(screenRow).join('')}</section>`;
};
const seg = STATES.slice().reverse().map((s) => counts[s] ? `<i class="${KEY[s]}" style="width:${(counts[s] / screens.length) * 100}%" title="${esc(s)}: ${counts[s]}"></i>` : '').join('');

const html = `<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ba Vía · Theo dõi</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap">
<style>
:root{--bg:#121318;--card:#1A1C23;--line:#2A2D37;--ink:#ECEDF2;--ink2:#A2A6B4;--ink3:#6E7282;--acc:#8B93FF;--teal:#3CCB9C;--amber:#E7B34B;--violet:#B48CFF;--red:#F07167;--mono:"JetBrains Mono",ui-monospace,Consolas,monospace;color-scheme:dark}
@media (prefers-color-scheme:light){:root{--bg:#F6F6F9;--card:#FFFFFF;--line:#E3E4EB;--ink:#1A1C23;--ink2:#5A5F6E;--ink3:#8B8F9C;--acc:#4F57E8;--teal:#119C6E;--amber:#B9800E;--violet:#7A4FE0;--red:#D2463B;color-scheme:light}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 "Be Vietnam Pro",system-ui,sans-serif}
.wrap{max-width:920px;margin:0 auto;padding:40px max(16px,env(safe-area-inset-right)) 80px max(16px,env(safe-area-inset-left))}
.eyebrow{font:700 12px var(--mono);letter-spacing:.14em;color:var(--ink3);text-transform:uppercase}
h1{font-size:clamp(30px,6vw,40px);font-weight:800;margin:4px 0 8px;letter-spacing:-.01em}
h2{font-size:22px;font-weight:800;margin:44px 0 4px}
h3{font-size:17px;font-weight:800;margin:0}
.sub{color:var(--ink2);margin:0;max-width:70ch}
.upd{color:var(--ink3);font-size:13px;margin:22px 0 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px}
.mono{font-family:var(--mono);color:var(--ink3);font-size:12.5px}
.hero{margin-top:28px;padding:22px 22px 18px}
.hero .top{display:flex;justify-content:space-between;align-items:flex-end;gap:16px;flex-wrap:wrap}
.big{font:700 clamp(30px,6vw,42px)/1 var(--mono)}
.big small{font-size:16px;color:var(--ink3)}
.hero .r{text-align:right}
.track{position:relative;height:10px;border-radius:5px;background:var(--line);margin:22px 0 8px;overflow:hidden;display:flex}
.track i{display:block;height:100%}
i.done{background:var(--teal)} i.building{background:var(--violet)} i.designed{background:var(--acc)} i.designing{background:var(--amber)}
.legend{display:flex;flex-wrap:wrap;gap:6px 16px;font:12px var(--mono);color:var(--ink3)}
.legend b{color:var(--ink)}
.dot{display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:6px;vertical-align:0}
.stats{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:14px;overflow:hidden}
.stats>div{padding:16px;border-left:1px solid var(--line)}
.stats>div:first-child{border-left:0}
.stats b{display:block;font:700 26px/1.1 var(--mono)}
.stats span{font-size:13px;color:var(--ink2)}
.stats small{display:block;font:12px var(--mono);color:var(--ink3);margin-top:2px}
.flow{margin-top:14px;padding:16px 16px 6px}
.flow header{display:flex;justify-content:space-between;align-items:baseline;gap:10px;flex-wrap:wrap}
.badge{font:700 10.5px var(--mono);letter-spacing:.08em;background:color-mix(in srgb,var(--acc) 22%,transparent);color:var(--acc);padding:3px 7px;border-radius:5px;vertical-align:2px}
.mini{height:4px;border-radius:2px;background:var(--line);margin:10px 0 6px;overflow:hidden}
.mini i{display:block;height:100%;background:var(--acc)}
.row{border-top:1px solid var(--line)}
.row summary{list-style:none;display:grid;grid-template-columns:20px 46px minmax(0,1fr) auto;gap:10px;align-items:center;padding:11px 2px;cursor:pointer}
.row summary::-webkit-details-marker{display:none}
.chk{width:18px;height:18px;border-radius:5px;border:2px solid var(--line);display:grid;place-items:center}
.row.done .chk{background:var(--teal);border-color:var(--teal)}
.row.done .chk::after{content:"";width:5px;height:9px;border:solid #fff;border-width:0 2px 2px 0;transform:rotate(45deg) translate(-1px,-1px)}
.row.designed .chk,.row.building .chk{border-color:var(--acc);background:color-mix(in srgb,var(--acc) 25%,transparent)}
.row.designing .chk{border-color:var(--amber)}
.rid{font:600 12.5px var(--mono);color:var(--ink3)}
.rn{font-weight:600;min-width:0}
.rn small{display:block;font-weight:400;font-size:12.5px;color:var(--ink3)}
.row.done .rn{color:var(--ink3);text-decoration:line-through}
.tags{display:flex;gap:6px;align-items:center}
.tg{font:600 11px var(--mono);color:var(--ink3);border:1px solid var(--line);padding:2px 6px;border-radius:5px}
.pill{font:700 11px var(--mono);padding:3px 8px;border-radius:5px;white-space:nowrap;background:var(--line);color:var(--ink2)}
.pill.designing{background:color-mix(in srgb,var(--amber) 20%,transparent);color:var(--amber)}
.pill.designed{background:color-mix(in srgb,var(--acc) 20%,transparent);color:var(--acc)}
.pill.building{background:color-mix(in srgb,var(--violet) 20%,transparent);color:var(--violet)}
.pill.done{background:color-mix(in srgb,var(--teal) 20%,transparent);color:var(--teal)}
.det{padding:0 4px 14px 76px;font-size:14px;color:var(--ink2)}
.det h5{margin:10px 0 2px;font:700 11px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink3)}
.det p{margin:0}.det ul{margin:0;padding-left:18px}
.det .pur{color:var(--ink)}
.list{margin-top:14px}
.li{display:grid;grid-template-columns:44px minmax(0,1fr) auto;gap:10px;padding:13px 16px;border-top:1px solid var(--line);align-items:start}
.li:first-child{border-top:0}
.li p{margin:2px 0 0;font-size:13.5px;color:var(--ink2)}
.li .chosen{color:var(--teal);font-weight:600}
.log{margin:14px 0 0;padding:14px 16px 14px 34px;font-size:14px;color:var(--ink2)}
code{font-family:var(--mono);font-size:.9em}
footer{margin-top:40px;color:var(--ink3);font-size:13px}
a{color:var(--acc)}
@media (max-width:620px){.stats{grid-template-columns:1fr 1fr}.stats>div:nth-child(3){border-left:0}.stats>div:nth-child(n+3){border-top:1px solid var(--line)}.row summary{grid-template-columns:20px 40px minmax(0,1fr)}.row .tags{grid-column:3}.det{padding-left:4px}.li{grid-template-columns:40px minmax(0,1fr)}.li>.pill{grid-column:2;justify-self:start}}
</style></head><body><div class="wrap">
<div class="eyebrow">Ba Vía · app tập gym</div>
<h1>Theo dõi tiến độ</h1>
<p class="sub">96 màn hình xếp theo thứ tự người dùng gặp. Trang tự sinh từ <code>TRACKING.md</code>: sửa file đó (trên máy hoặc ngay trên GitHub), đẩy lên là trang tự cập nhật.</p>
<p class="upd">Cập nhật lần cuối: ${esc(updated)}</p>

<section class="card hero">
  <div class="top">
    <div><div class="eyebrow">Bản đầu đã thiết kế</div><div class="big">${nDesigned}<small> / ${mvp.length} màn</small></div></div>
    <div class="r"><div class="eyebrow">Giai đoạn hiện tại</div><div style="font-weight:700;margin-top:4px">${curPhase ? `${esc(curPhase.id)} · ${esc(curPhase.name)}` : 'Đã xong tất cả'}</div></div>
  </div>
  <div class="track">${seg}</div>
  <div class="legend">${STATES.map((s) => `<span><span class="dot" style="background:${{ 'Chưa làm': 'var(--line)', 'Đang thiết kế': 'var(--amber)', 'Đã thiết kế': 'var(--acc)', 'Đang code': 'var(--violet)', 'Xong': 'var(--teal)' }[s]}"></span>${esc(s)} <b>${counts[s]}</b></span>`).join('')}</div>
</section>
<section class="card stats">
  <div><b>${pct(nDesigned, mvp.length)}%</b><span>Bản đầu đã thiết kế</span><small>${nDesigned}/${mvp.length} màn</small></div>
  <div><b>${pct(nDone, mvp.length)}%</b><span>Bản đầu đã code xong</span><small>${nDone}/${mvp.length} màn</small></div>
  <div><b>${nPhaseDone}/${phases.length}</b><span>Giai đoạn xong</span><small>lộ trình</small></div>
  <div><b>${nDecided}/${decisions.length}</b><span>Quyết định đã chốt</span><small>${decisions.length - nDecided} còn chờ</small></div>
</section>

<h2>Màn hình</h2>
<p class="sub">Bấm vào một màn để xem chi tiết.</p>
${flows.map(flowCard).join('\n')}

<h2>Quyết định cần chốt</h2>
<p class="sub">Ghi phương án đã chọn vào cột “Đã chốt” trong TRACKING.md.</p>
<section class="card list">${decisions.map((d) => `<div class="li"><span class="rid">${esc(d.id)}</span><div><b>${esc(d.q)}</b>${d.chosen ? `<p class="chosen">Đã chốt: ${inline(d.chosen)}</p>` : `<p>Fable đề xuất: ${inline(d.rec)}</p>`}${decInfo[d.id] && !d.chosen ? `<p>Phương án: ${decInfo[d.id].options_vi.map(esc).join(' · ')}</p>` : ''}</div><span class="pill ${d.chosen ? 'done' : ''}">${d.chosen ? 'Đã chốt' : 'Chờ chốt'}</span></div>`).join('')}</section>

<h2>Lộ trình</h2>
<section class="card list">${phases.map((p) => `<div class="li"><span class="rid">${esc(p.id)}</span><div><b>${esc(p.name)}</b><p>${esc((phaseInfo[p.id] || {}).goal_vi || '')} · khoảng ${esc(p.effort)} buổi</p></div><span class="pill ${KEY[p.st] || ''}">${esc(p.st)}</span></div>`).join('')}</section>

<h2>Nhật ký</h2>
<ul class="card log">${log.map((l) => `<li>${inline(l)}</li>`).join('')}</ul>
<footer>Nguồn: <code>TRACKING.md</code> · chi tiết màn: <code>design/screens.json</code> · kế hoạch đầy đủ: <code>design/08-screen-plan.md</code></footer>
</div></body></html>
`;
fs.mkdirSync(path.join(root, 'docs'), { recursive: true });
fs.writeFileSync(path.join(root, 'docs', 'index.html'), html);
console.log(`docs/index.html: ${screens.length} màn, ${nDesigned}/${mvp.length} bản đầu đã thiết kế, ${nDecided}/${decisions.length} quyết định`);
