// cataclysm:witherite_ingot -> gates the EV machine hull (The Harbinger)
ServerEvents.recipes(event => {
  global.gateHull(event, {
    tier: 'ev',
    boss: 'cataclysm:witherite_ingot',
    bossName: 'The Harbinger',
    cables: ['aluminium'],
    plateOuter: 'polyethylene',
    plateInner: 'titanium',
    fluid: 'gtceu:polyethylene'
  });
});
