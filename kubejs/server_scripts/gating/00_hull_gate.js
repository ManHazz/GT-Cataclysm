// Shared helper: rebuilds every recipe that produces a GT machine hull so it
// also needs a Cataclysm boss drop. Original GT ingredients are kept as-is.
// Loaded first (00_ prefix); tier files call global.gateHull(event, cfg).
global.GATED_HULLS = global.GATED_HULLS || {};

global.gateHull = function (event, cfg) {
  const hull = `gtceu:${cfg.tier}_machine_hull`;
  const casing = `gtceu:${cfg.tier}_machine_casing`;
  global.GATED_HULLS[hull] = { boss: cfg.bossName, item: cfg.boss };

  // Drop original crafting + assembler recipes (ids verified from a boot log).
  event.remove({ output: hull });

  // Crafting table: original PLP/CHC layout plus the boss item in the bottom row.
  event.shaped(Item.of(hull), ['PLP', 'CHC', ' B '], {
    P: `#forge:plates/${cfg.plateOuter}`,
    L: `#forge:plates/${cfg.plateInner}`,
    C: `gtceu:${cfg.cables[0]}_single_cable`,
    H: casing,
    B: cfg.boss
  }).id(`kubejs:gated/${cfg.tier}_machine_hull_shaped`);

  // Assembler: one recipe per cable variant (MV also accepts annealed copper).
  cfg.cables.forEach((cable, i) => {
    event.recipes.gtceu.assembler(`kubejs:gated/hull_${cfg.tier}${i ? '_' + cable : ''}`)
      .itemInputs(casing, `2x gtceu:${cable}_single_cable`, cfg.boss)
      .inputFluids(`${cfg.fluid} 288`)
      .itemOutputs(hull)
      .duration(50)
      .EUt(16);
  });
};
