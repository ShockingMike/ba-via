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
  var ICONS = {
 "homnay": "<mask id=\"{{id}}\" maskUnits=\"userSpaceOnUse\" x=\"0\" y=\"0\" width=\"24\" height=\"24\"><rect width=\"24\" height=\"24\" fill=\"#fff\" stroke=\"none\"/><g class=\"ni-db\" style=\"transform-origin:12.6px 20.7px\"><g transform=\"rotate(-12 12.6 15.2)\" fill=\"#000\" stroke=\"#000\" stroke-width=\"4.4\"><rect x=\"3\" y=\"10.9\" width=\"5.3\" height=\"8.6\" rx=\"2.4\"/><rect x=\"16.9\" y=\"10.9\" width=\"5.3\" height=\"8.6\" rx=\"2.4\"/><path d=\"M8.3 13.5h8.6v3.4H8.3z\"/></g></g></mask><g mask=\"url(#{{id}})\"><g class=\"ni-sun\" style=\"transform-origin:7.9px 6.7px\"><g class=\"ni-tint\" fill=\"currentColor\" stroke=\"none\" opacity=\"0\"><circle cx=\"7.9\" cy=\"6.7\" r=\"2.6\"/></g><circle cx=\"7.9\" cy=\"6.7\" r=\"2.6\"/><path d=\"M12.30 6.70L13.70 6.70M11.01 3.59L12.00 2.60M7.90 2.30L7.90 0.90M4.79 3.59L3.80 2.60M3.50 6.70L2.10 6.70\"/></g></g><g class=\"ni-db\" style=\"transform-origin:12.6px 20.7px\"><g transform=\"rotate(-12 12.6 15.2)\"><g class=\"ni-tint\" fill=\"currentColor\" stroke=\"none\" opacity=\"0\"><rect x=\"3\" y=\"10.9\" width=\"5.3\" height=\"8.6\" rx=\"2.4\"/><rect x=\"16.9\" y=\"10.9\" width=\"5.3\" height=\"8.6\" rx=\"2.4\"/><path d=\"M8.3 13.5h8.6v3.4H8.3z\"/></g><rect x=\"3\" y=\"10.9\" width=\"5.3\" height=\"8.6\" rx=\"2.4\"/><rect x=\"16.9\" y=\"10.9\" width=\"5.3\" height=\"8.6\" rx=\"2.4\"/><path d=\"M8.3 13.5h8.6M8.3 16.9h8.6\"/></g></g>",
 "hoi": "<mask id=\"{{id}}\" maskUnits=\"userSpaceOnUse\" x=\"0\" y=\"0\" width=\"24\" height=\"24\"><rect width=\"24\" height=\"24\" fill=\"#fff\" stroke=\"none\"/><g class=\"ni-hand-r\" style=\"transform-origin:17.4px 20.4px\"><path transform=\"translate(16.9 19.6) scale(-1 1) rotate(21)\" d=\"M-3.43 0.51-3.81-3.05C-5.59-3.81-7.24-5.33-7.49-6.99-7.75-8.64-5.97-9.4-4.95-8.26L-3.81-6.99V-10.54C-3.81-12.19-2.54-13.34-1.02-13.34H1.02C2.54-13.34 3.81-12.19 3.81-10.54V-3.05L3.43 0.51Z\" fill=\"#000\" stroke=\"#000\" stroke-width=\"4\"/></g></mask><g mask=\"url(#{{id}})\"><g class=\"ni-hand-l\" style=\"transform-origin:6.6px 21px\"><g transform=\"translate(6.5 20.1) rotate(18)\"><g class=\"ni-tint\" fill=\"currentColor\" stroke=\"none\" opacity=\"0\"><path d=\"M-3.43 0.51-3.81-3.05C-5.59-3.81-7.24-5.33-7.49-6.99-7.75-8.64-5.97-9.4-4.95-8.26L-3.81-6.99V-10.54C-3.81-12.19-2.54-13.34-1.02-13.34H1.02C2.54-13.34 3.81-12.19 3.81-10.54V-3.05L3.43 0.51Z\"/></g><path d=\"M-3.43 0.51-3.81-3.05C-5.59-3.81-7.24-5.33-7.49-6.99-7.75-8.64-5.97-9.4-4.95-8.26L-3.81-6.99V-10.54C-3.81-12.19-2.54-13.34-1.02-13.34H1.02C2.54-13.34 3.81-12.19 3.81-10.54V-3.05L3.43 0.51Z\"/></g></g></g><g class=\"ni-hand-r\" style=\"transform-origin:17.4px 20.4px\"><g transform=\"translate(16.9 19.6) scale(-1 1) rotate(21)\"><g class=\"ni-tint\" fill=\"currentColor\" stroke=\"none\" opacity=\"0\"><path d=\"M-3.43 0.51-3.81-3.05C-5.59-3.81-7.24-5.33-7.49-6.99-7.75-8.64-5.97-9.4-4.95-8.26L-3.81-6.99V-10.54C-3.81-12.19-2.54-13.34-1.02-13.34H1.02C2.54-13.34 3.81-12.19 3.81-10.54V-3.05L3.43 0.51Z\"/></g><path d=\"M-3.43 0.51-3.81-3.05C-5.59-3.81-7.24-5.33-7.49-6.99-7.75-8.64-5.97-9.4-4.95-8.26L-3.81-6.99V-10.54C-3.81-12.19-2.54-13.34-1.02-13.34H1.02C2.54-13.34 3.81-12.19 3.81-10.54V-3.05L3.43 0.51Z\"/></g></g><path class=\"ni-burst\" style=\"transform-origin:12px 6.5px\" d=\"M11.8 1.5v2.2M7.6 4 6.3 2.3M15.9 3.2l1.3-1.7\"/>",
 "tudo": "<g class=\"ni-body\"><g class=\"ni-tint\" fill=\"currentColor\" stroke=\"none\" opacity=\"0\"><rect x=\"3.6\" y=\"2.6\" width=\"9.8\" height=\"17.4\" rx=\"1.8\"/></g><rect x=\"3.6\" y=\"2.6\" width=\"9.8\" height=\"17.4\" rx=\"1.8\"/><path d=\"M6.6 6.4h3.8M6.6 9.2h3.8M5.6 20v1.6M11.4 20v1.6\"/></g><path class=\"ni-sock\" opacity=\"0\" style=\"transform-origin:13.4px 19.6px\" d=\"M14.3 18.2h2.3a1.5 1.5 0 0 1 0 3h-2.3\"/><g class=\"ni-door\" style=\"transform-origin:13.4px 11px\"><g class=\"ni-tint\" fill=\"currentColor\" stroke=\"none\" opacity=\"0\"><path d=\"M13.4 4l5.5 1.7a1.2 1.2 0 0 1 .9 1.2v8.6a1.2 1.2 0 0 1-.9 1.2l-5.5 1.9\"/></g><path d=\"M13.4 4l5.5 1.7a1.2 1.2 0 0 1 .9 1.2v8.6a1.2 1.2 0 0 1-.9 1.2l-5.5 1.9\"/><path d=\"M16.7 10.4v1.8\"/></g>"
};
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
