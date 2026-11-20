// Recompute the "Tóm tắt" block in TRACKING.md from the tables in the same file.
// Usage (from C:\Work\GymApp):  node tools/tracking-summary.js
const fs = require('fs');
const path = require('path');
const file = path.join(__dirname, '..', 'TRACKING.md');
const md = fs.readFileSync(file, 'utf8');

const STATES = ['Chưa làm', 'Đang thiết kế', 'Đã thiết kế', 'Đang code', 'Xong'];
const screens = [];
const phases = [];
const decisions = [];
let section = '';
for (const line of md.split('\n')) {
  if (line.startsWith('## ')) section = line.slice(3).trim();
  if (!line.startsWith('|') || line.startsWith('|---') || line.startsWith('| Mã')) continue;
  const c = line.split('|').slice(1, -1).map((s) => s.trim());
  if (section.startsWith('Màn hình')) screens.push({ id: c[0], pri: c[2], st: c[3] });
  else if (section.startsWith('Lộ trình')) phases.push({ id: c[0], st: c[3] });
  else if (section.startsWith('Quyết định')) decisions.push({ id: c[0], chosen: c[3] });
}

const bad = screens.filter((s) => !STATES.includes(s.st)).map((s) => `${s.id} ("${s.st}")`);
const count = (list, pred) => list.filter(pred).length;
const designedOrLater = (s) => ['Đã thiết kế', 'Đang code', 'Xong'].includes(s.st);
const mvp = screens.filter((s) => s.pri === 'Bản đầu');

const lines = [
  `- Tổng: **${screens.length}** màn, trong đó **${mvp.length}** thuộc bản đầu.`,
  `- Bản đầu đã thiết kế: **${count(mvp, designedOrLater)}/${mvp.length}** · đã code xong: **${count(mvp, (s) => s.st === 'Xong')}/${mvp.length}**.`,
  `- Theo trạng thái (mọi bản): ${STATES.map((st) => `${st} ${count(screens, (s) => s.st === st)}`).join(' · ')}.`,
  `- Giai đoạn xong: **${count(phases, (p) => p.st === 'Xong')}/${phases.length}** · quyết định đã chốt: **${count(decisions, (d) => d.chosen)}/${decisions.length}**.`,
  `- Cập nhật lúc: ${new Date().toISOString().slice(0, 16).replace('T', ' ')}.`,
];
if (bad.length) lines.push(`- ⚠ Trạng thái không hợp lệ: ${bad.join(', ')}.`);

const out = md.replace(/<!-- SUMMARY:START -->[\s\S]*?<!-- SUMMARY:END -->/, `<!-- SUMMARY:START -->\n${lines.join('\n')}\n<!-- SUMMARY:END -->`);
fs.writeFileSync(file, out);
console.log(lines.join('\n'));
