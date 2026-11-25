/* Tạ Nhỏ · nav icons + tap animations. Self-contained: no CSS file, no dependencies.
 *
 * Markup it expects (class names are the contract):
 *   <nav class="navbar">
 *     <button class="tab" data-icon="homnay" aria-current="page">Hôm nay</button>
 *     <button class="tab" data-icon="hoi">Hội</button>
 *     <button class="tab" data-icon="tudo">Tủ đồ</button>
 *   </nav>
 *   <script src="nav-icons/nav-anim.js"></script>
 *
 * On load it (1) draws the icon into every .tab[data-icon] that has no <svg> yet, as the first child,
 * (2) on a tap marks that tab current (class "on" + aria-current="page"), clears the others,
 * plays the icon's animation and pops the dot (.tab em or .tab .dot, if there is one),
 * (3) fires a bubbling "navtab" CustomEvent on the tab, detail = {icon: "hoi"}, for routing.
 * The icon uses currentColor; the current tab gets the soft fill and the heavier stroke from the CSS below.
 * prefers-reduced-motion: one small scale pop instead of the moving parts.
 * Bars added later: TaNhoNav.init(rootElement). Manual: TaNhoNav.select(tab), TaNhoNav.play(tab), TaNhoNav.svg("hoi").
 */
(function () {
  'use strict';
  var ICONS = /*ICONS*/{};
  var CSS = '.navbar .tab svg.ni{display:block;overflow:visible;stroke-width:1.9;transition:stroke-width .18s ease-out}' +
    '.navbar .tab[aria-current="page"] svg.ni{stroke-width:2.3}' +
    '.navbar .tab svg.ni .ni-tint{opacity:0;transition:opacity .18s ease-out}' +
    '.navbar .tab[aria-current="page"] svg.ni .ni-tint{opacity:.2}';
  var POP = 'cubic-bezier(.34,1.56,.64,1)', OUT = 'cubic-bezier(.22,1,.36,1)';
  var n = 0;
  var reduced = window.matchMedia ? window.matchMedia('(prefers-reduced-motion: reduce)') : { matches: false };

  function svg(name, size) {
    size = size || 28;
    return '<svg class="ni" data-icon="' + name + '" width="' + size + '" height="' + size + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
      'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + ICONS[name].split('{{id}}').join('ni-k' + (++n)) + '</svg>';
  }
  function run(root, sel, frames, ms, easing) {
    var out = [];
    root.querySelectorAll(sel).forEach(function (el) {
      if (el.animate) out.push(el.animate(frames, { duration: ms, easing: easing || 'ease-out' }));
    });
    return out;
  }
  var ANIM = {
    // the dumbbell hops and lands with a small squash; the sun behind it swells and rocks once (a twinkle)
    homnay: function (s) {
      return run(s, '.ni-db', [
        { transform: 'translateY(0) scale(1,1)' },
        { transform: 'translateY(-2.6px) scale(.96,1.06)', offset: .34 },
        { transform: 'translateY(.2px) scale(1.07,.9)', offset: .64 },
        { transform: 'translateY(0) scale(.99,1.02)', offset: .84 },
        { transform: 'translateY(0) scale(1,1)' }], 520)
        .concat(run(s, '.ni-sun', [
          { transform: 'rotate(0deg) scale(1)' },
          { transform: 'rotate(-16deg) scale(1.16)', offset: .4 },
          { transform: 'rotate(8deg) scale(1.04)', offset: .72 },
          { transform: 'rotate(0deg) scale(1)' }], 560));
    },
    // the palms pull apart, clap a touch past rest, settle; the burst pops out at the moment of contact
    hoi: function (s) {
      function swing(sign) {
        return [{ transform: 'rotate(0deg)' },
          { transform: 'rotate(' + (-13 * sign) + 'deg)', offset: .36 },
          { transform: 'rotate(' + (4 * sign) + 'deg)', offset: .62 },
          { transform: 'rotate(' + (-1 * sign) + 'deg)', offset: .82 },
          { transform: 'rotate(0deg)' }];
      }
      return run(s, '.ni-hand-l', swing(1), 500).concat(run(s, '.ni-hand-r', swing(-1), 500),
        run(s, '.ni-burst', [
          { opacity: 0, transform: 'scale(.4)' },
          { opacity: 0, transform: 'scale(.4)', offset: .5 },
          { opacity: 1, transform: 'scale(1.3)', offset: .74 },
          { opacity: 1, transform: 'scale(1)' }], 520));
    },
    // the door swings to and back with a little overshoot; a sock tip peeks out underneath, then ducks back in
    tudo: function (s) {
      return run(s, '.ni-door', [
        { transform: 'scaleX(1)' },
        { transform: 'scaleX(.52)', offset: .34 },
        { transform: 'scaleX(.52)', offset: .56 },
        { transform: 'scaleX(1.1)', offset: .82 },
        { transform: 'scaleX(1)' }], 600)
        .concat(run(s, '.ni-sock', [
          { opacity: 0, transform: 'scaleX(0)' },
          { opacity: 1, transform: 'scaleX(0)', offset: .16 },
          { opacity: 1, transform: 'scaleX(1.12)', offset: .4 },
          { opacity: 1, transform: 'scaleX(1)', offset: .58 },
          { opacity: 1, transform: 'scaleX(0)', offset: .86 },
          { opacity: 0, transform: 'scaleX(0)' }], 600));
    }
  };
  function play(tab) {
    var s = tab.querySelector('svg.ni');
    if (!s || !s.animate) return [];
    (s.getAnimations ? s.getAnimations({ subtree: true }) : []).forEach(function (a) { a.cancel(); });
    if (reduced.matches) return [s.animate([{ transform: 'scale(1)' }, { transform: 'scale(1.1)' }, { transform: 'scale(1)' }], { duration: 200, easing: 'ease-out' })];
    var f = ANIM[s.getAttribute('data-icon')];
    var out = f ? f(s) : [];
    var dot = tab.querySelector('em,.dot');
    if (dot && dot.animate) out.push(dot.animate([{ transform: 'scale(0)' }, { transform: 'scale(1)' }], { duration: 380, easing: POP }));
    return out;
  }
  function select(tab, silent) {
    var bar = tab.closest('.navbar');
    if (!bar) return [];
    bar.querySelectorAll('.tab').forEach(function (t) {
      var on = t === tab;
      t.classList.toggle('on', on);
      t.setAttribute('aria-current', on ? 'page' : 'false');
    });
    var out = silent ? [] : play(tab);
    tab.dispatchEvent(new CustomEvent('navtab', { bubbles: true, detail: { icon: tab.getAttribute('data-icon') } }));
    return out;
  }
  function init(root) {
    root = root || document;
    if (!document.getElementById('ni-css')) {
      var st = document.createElement('style'); st.id = 'ni-css'; st.textContent = CSS; document.head.appendChild(st);
    }
    var bars = root.matches && root.matches('.navbar') ? [root] : root.querySelectorAll('.navbar');
    Array.prototype.forEach.call(bars, function (bar) {
      bar.querySelectorAll('.tab[data-icon]').forEach(function (t) {
        var k = t.getAttribute('data-icon');
        if (ICONS[k] && !t.querySelector('svg')) t.insertAdjacentHTML('afterbegin', svg(k));
      });
      if (bar.__ni) return;
      bar.__ni = true;
      bar.addEventListener('click', function (e) {
        var t = e.target.closest ? e.target.closest('.tab') : null;
        if (t && bar.contains(t)) select(t);
      });
    });
  }
  window.TaNhoNav = { init: init, select: select, play: play, svg: svg };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { init(document); });
  else init(document);
})();
