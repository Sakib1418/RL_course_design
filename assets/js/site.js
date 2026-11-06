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
