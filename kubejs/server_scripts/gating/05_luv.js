// cataclysm:cursium_ingot -> gates the LUV machine hull (Maledictus)
ServerEvents.recipes(event => {
  global.gateHull(event, {
    tier: 'luv',
    boss: 'cataclysm:cursium_ingot',
    bossName: 'Maledictus',
    cables: ['niobium_titanium'],
    plateOuter: 'polytetrafluoroethylene',
    plateInner: 'rhodium_plated_palladium',
    fluid: 'gtceu:polytetrafluoroethylene'
  });
});
