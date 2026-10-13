// Shared helper: rebuilds every recipe that produces a GT machine hull so it
// also needs a Cataclysm boss drop as a NOT-consumed catalyst (assembler only). Original GT ingredients are kept as-is.
// Loaded first (00_ prefix); tier files call global.gateHull(event, cfg).
global.GATED_HULLS = global.GATED_HULLS || {};

global.gateHull = function (event, cfg) {
  const hull = `gtceu:${cfg.tier}_machine_hull`;
  const casing = `gtceu:${cfg.tier}_machine_casing`;
  global.GATED_HULLS[hull] = { boss: cfg.bossName, item: cfg.boss };

  // Drop original crafting + assembler recipes (crafting table route is removed) (ids verified from a boot log).
  event.remove({ output: hull });

  // Assembler: one recipe per cable variant (MV also accepts annealed copper).
  cfg.cables.forEach((cable, i) => {
    event.recipes.gtceu.assembler(`kubejs:gated/hull_${cfg.tier}${i ? '_' + cable : ''}`)
      .itemInputs(casing, `2x gtceu:${cable}_single_cable`)
      .notConsumable(cfg.boss)
      .inputFluids(`${cfg.fluid} 288`)
      .itemOutputs(hull)
      .duration(50)
      .EUt(16);
  });
};
