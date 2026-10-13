// cataclysm:essence_of_the_storm -> gates the ZPM machine hull (Scylla)
ServerEvents.recipes(event => {
  global.gateHull(event, {
    tier: 'zpm',
    boss: 'cataclysm:essence_of_the_storm',
    bossName: 'Scylla',
    cables: ['vanadium_gallium'],
    plateOuter: 'polybenzimidazole',
    plateInner: 'naquadah_alloy',
    fluid: 'gtceu:polybenzimidazole'
  });
});
