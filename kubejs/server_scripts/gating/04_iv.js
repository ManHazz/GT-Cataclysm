// cataclysm:gauntlet_of_guard -> gates the IV machine hull (Ender Guardian)
ServerEvents.recipes(event => {
  global.gateHull(event, {
    tier: 'iv',
    boss: 'cataclysm:gauntlet_of_guard',
    bossName: 'Ender Guardian',
    cables: ['platinum'],
    plateOuter: 'polytetrafluoroethylene',
    plateInner: 'tungsten_steel',
    fluid: 'gtceu:polytetrafluoroethylene'
  });
});
