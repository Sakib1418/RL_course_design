// Feedback buttons: open the device's default mail app first; if nothing takes over,
// offer Gmail, then Outlook, then a LinkedIn message, plus copy-the-address.
const FB_LINKEDIN = 'https://www.linkedin.com/in/sakib-ferdous';
function fbLinks(email, subject) {
  const to = encodeURIComponent(email), s = encodeURIComponent(subject), b = encodeURIComponent('Hi Sakib,\n\n');
  return {
    mail: `mailto:${email}?subject=${s}&body=${b}`,
    alt: [
      ['Gmail', `https://mail.google.com/mail/?view=cm&fs=1&to=${to}&su=${s}&body=${b}`],
      ['Outlook', `https://outlook.live.com/mail/0/deeplink/compose?to=${to}&subject=${s}&body=${b}`],
      ['LinkedIn message', FB_LINKEDIN],
    ],
  };
}
function fbPanel(email, subject) {
  const l = fbLinks(email, subject);
  let d = document.getElementById('fb-dialog');
  if (!d) { d = document.createElement('dialog'); d.id = 'fb-dialog'; d.className = 'fb-dialog'; document.body.appendChild(d); }
  d.innerHTML = `<form method="dialog" class="fb-x"><button aria-label="Close">&times;</button></form>
    <p class="eyebrow">Feedback</p><h3>Send Sakib a message</h3>
    <p>Your mail app didn't open? Choose another way:</p>
    <div class="fb-options">${l.alt.map(([t, h], i) =>
      `<a class="btn ${i === 0 ? 'primary' : 'ghost'}" href="${h}" target="_blank" rel="noopener">${i + 1}. ${t}</a>`).join('')}</div>
    <p class="fb-more"><a href="${l.mail}">Try the mail app again</a> &middot; or copy
      <button type="button" class="fb-copy">${email}</button></p>`;
  const c = d.querySelector('.fb-copy');
  c.onclick = () => navigator.clipboard?.writeText(email).then(() => { c.textContent = 'Copied ✓'; });
  if (d.showModal) d.showModal(); else d.setAttribute('open', '');
}
document.addEventListener('click', (e) => {
  const a = e.target.closest && e.target.closest('a.js-feedback');
  if (!a) return;
  e.preventDefault();
  const email = a.dataset.email, subject = a.dataset.subject || 'Feedback';
  let left = false;
  const mark = () => { left = true; };
  const vis = () => { if (document.hidden) left = true; };
  window.addEventListener('blur', mark);
  document.addEventListener('visibilitychange', vis);
  window.location.href = fbLinks(email, subject).mail;          // 1st: default mail app (phones, desktop clients)
  setTimeout(() => {
    window.removeEventListener('blur', mark);
    document.removeEventListener('visibilitychange', vis);
    if (!left) fbPanel(email, subject);                          // then: Gmail, Outlook, LinkedIn
  }, 1600);
});

// Renders ```mermaid diagrams in the page's accent colour.
const blocks = document.querySelectorAll('pre.mermaid');
if (blocks.length) {
  const { default: mermaid } = await import('https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.esm.min.mjs');
  const css = getComputedStyle(document.body);
  const accent = css.getPropertyValue('--accent').trim() || '#750014';
  const soft = css.getPropertyValue('--accent-soft').trim() || '#F6E9EA';
  mermaid.initialize({
    startOnLoad: false,
    theme: 'base',
    fontFamily: 'Inter, system-ui, sans-serif',
    flowchart: { curve: 'basis', padding: 14, nodeSpacing: 36, rankSpacing: 44, useMaxWidth: true },
    themeVariables: {
      fontSize: '15px',
      primaryColor: soft,
      primaryBorderColor: accent,
      primaryTextColor: '#212326',
      lineColor: accent,
      secondaryColor: '#F7F6F0',
      tertiaryColor: '#FFFFFF',
      edgeLabelBackground: '#FFFFFF',
      clusterBkg: '#F7F6F0',
      clusterBorder: '#DDD9CB',
    },
  });
  await mermaid.run({ nodes: blocks });
}
document.documentElement.classList.add('ready');
