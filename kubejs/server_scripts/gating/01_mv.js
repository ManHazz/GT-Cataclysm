// cataclysm:monstrous_horn -> gates the MV machine hull (Netherite Monstrosity)
ServerEvents.recipes(event => {
  global.gateHull(event, {
    tier: 'mv',
    boss: 'cataclysm:monstrous_horn',
    bossName: 'Netherite Monstrosity',
    cables: ['copper', 'annealed_copper'],
    plateOuter: 'wrought_iron',
    plateInner: 'aluminium',
    fluid: 'gtceu:polyethylene'
  });
});
