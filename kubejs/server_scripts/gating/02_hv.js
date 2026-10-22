// cataclysm:ignitium_ingot -> gates the HV machine hull (Ignis)
ServerEvents.recipes(event => {
  global.gateHull(event, {
    tier: 'hv',
    boss: 'cataclysm:ignitium_ingot',
    bossName: 'Ignis',
    cables: ['gold'],
    plateOuter: 'polyethylene',
    plateInner: 'stainless_steel',
    fluid: 'gtceu:polyethylene'
  });
});
