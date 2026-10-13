// Tooltips on gated machine hulls naming the required boss drop.
ItemEvents.tooltip(event => {
  const gates = {
    'gtceu:mv_machine_hull':  ['Netherite Monstrosity', 'cataclysm:monstrous_horn'],
    'gtceu:hv_machine_hull':  ['Ignis', 'cataclysm:ignitium_ingot'],
    'gtceu:ev_machine_hull':  ['The Harbinger', 'cataclysm:witherite_ingot'],
    'gtceu:iv_machine_hull':  ['Ender Guardian', 'cataclysm:gauntlet_of_guard'],
    'gtceu:luv_machine_hull': ['Maledictus', 'cataclysm:cursium_ingot'],
    'gtceu:zpm_machine_hull': ['Scylla', 'cataclysm:essence_of_the_storm']
  };
  Object.keys(gates).forEach(id => {
    const boss = gates[id][0];
    const drop = Item.of(gates[id][1]).getHoverName();
    event.add(id, Text.gold('Requires ').append(Text.yellow(drop)).append(Text.gold(' (not consumed) - ' + boss)));
  });
});
