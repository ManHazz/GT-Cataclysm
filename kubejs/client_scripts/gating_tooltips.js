// Wrapped tooltips (max 40 chars/line) for gated hulls, boss catalysts, dungeon eyes, quest book.
const WRAP = 40;
function wrap(str) {
  const out = [];
  let line = '';
  String(str).split(' ').forEach(w => {
    if (line.length && (line + ' ' + w).length > WRAP) { out.push(line); line = w; }
    else line = line.length ? line + ' ' + w : w;
  });
  if (line.length) out.push(line);
  return out;
}
function lines(str, color) {
  return wrap(str).map(l => Text.of(l).color(color));
}

ItemEvents.tooltip(event => {
  const tiers = [
    ['mv',  'Netherite Monstrosity', 'monstrous_horn',        'Monstrous Horn'],
    ['hv',  'Ignis',                 'ignitium_ingot',        'Ignitium Ingot'],
    ['ev',  'The Harbinger',         'witherite_ingot',       'Witherite Ingot'],
    ['iv',  'Ender Guardian',        'gauntlet_of_guard',     'Gauntlet of Guard'],
    ['luv', 'Maledictus',            'cursium_ingot',         'Cursium Ingot'],
    ['zpm', 'Scylla',                'essence_of_the_storm',  'Essence of the Storm']
  ];
  tiers.forEach(t => {
    const tier = t[0].toUpperCase();
    event.add('gtceu:' + t[0] + '_machine_hull',
      lines('Gated. Needs ' + t[3] + ' from ' + t[1] + ' as a catalyst in the Assembler. Not consumed.', 'yellow'));
    event.add('cataclysm:' + t[2],
      lines('Dropped by ' + t[1] + '. Unlocks the ' + tier + ' Machine Hull. Not consumed in the recipe.', 'yellow'));
  });

  const eyes = {
    monstrous: 'the Soul Black Smith',
    flame: 'the Burning Arena',
    mech: 'the Ancient Factory',
    void: 'the Ruined Citadel',
    cursed: 'the Frosted Prison',
    storm: 'the Acropolis',
    abyss: 'the Sunken City',
    desert: 'the Cursed Pyramid'
  };
  Object.keys(eyes).forEach(k => {
    event.add('cataclysm:' + k + '_eye', lines('Locates a Cataclysm structure: ' + eyes[k] + '.', 'gray'));
  });

  event.add('heracles:quest_book', lines('Right-click to open. Key: J.', 'gray'));
});
