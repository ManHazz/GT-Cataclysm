// PonderJS 2.x (Ponder 1.0.92): Ponder.registry fires client-side.
// Helpers: place a block hidden, then reveal it from above with a short idle.
function gtcPut(scene, util, x, y, z, id) {
  const p = util.grid.at(x, y, z)
  scene.world.setBlock(p, id, false)
  return p
}
function gtcShow(scene, util, x, y, z, ticks) {
  scene.world.showSection(util.select.position(x, y, z), Direction.DOWN)
  scene.idle(ticks === undefined ? 6 : ticks)
}
function gtcText(scene, util, x, y, z, str, ticks) {
  scene.overlay.showText(ticks || 60)
    .text(str)
    .pointAt(util.vector.topOf(x, y, z))
    .placeNearTarget()
  scene.idle((ticks || 60) + 10)
}
function gtcNote(scene, str, ticks) {
  scene.overlay.showText(ticks || 60).text(str).independent(40)
  scene.idle((ticks || 60) + 10)
}

Ponder.registry(event => {
  // ---------------------------------------------------------------- LV macerator
  event.create('gtceu:lv_macerator')
    .scene('gtc_lv_macerator', 'The LV Macerator', (scene, util) => {
      scene.showBasePlate()
      scene.idle(10)

      const machine = util.grid.at(2, 1, 2)
      const cable = util.grid.at(3, 1, 2)

      scene.world.setBlock(machine, 'gtceu:lv_macerator', true)
      scene.world.showSection(util.select.position(machine), Direction.DOWN)
      scene.idle(10)

      scene.overlay.showText(60)
        .text('Insert ores here')
        .pointAt(util.vector.topOf(machine))
        .placeNearTarget()
      scene.idle(70)

      scene.world.setBlock(cable, 'gtceu:tin_single_cable', true)
      scene.world.showSection(util.select.position(cable), Direction.DOWN)
      scene.idle(10)

      scene.overlay.showText(60)
        .text('Power it with an LV cable')
        .pointAt(util.vector.topOf(cable))
        .placeNearTarget()
      scene.idle(70)
    })

  // ---------------------------------------------------------------- Electric Blast Furnace
  event.create('gtceu:electric_blast_furnace')
    .scene('gtc_electric_blast_furnace', 'The Electric Blast Furnace', (scene, util) => {
      scene.configureBasePlate(0, 0, 5)
      scene.scaleSceneView(0.85)
      scene.showBasePlate()
      scene.idle(10)

      const CASING = 'gtceu:heatproof_machine_casing'
      const COIL = 'gtceu:cupronickel_coil_block'

      // Pre-place everything hidden. Structure occupies x1-3, z1-3, y1-4.
      for (let x = 1; x <= 3; x++) {
        for (let z = 1; z <= 3; z++) {
          scene.world.setBlock(util.grid.at(x, 1, z), CASING, false)
          scene.world.setBlock(util.grid.at(x, 4, z), CASING, false)
          for (let y = 2; y <= 3; y++) {
            if (x === 2 && z === 2) continue
            scene.world.setBlock(util.grid.at(x, y, z), COIL, false)
          }
        }
      }
      scene.world.setBlock(util.grid.at(2, 1, 3), 'gtceu:electric_blast_furnace[facing=south]', false)
      scene.world.setBlock(util.grid.at(1, 1, 3), 'gtceu:lv_input_bus[facing=south]', false)
      scene.world.setBlock(util.grid.at(3, 1, 3), 'gtceu:lv_output_bus[facing=south]', false)
      scene.world.setBlock(util.grid.at(1, 1, 2), 'gtceu:lv_energy_input_hatch[facing=west]', false)
      scene.world.setBlock(util.grid.at(3, 1, 2), 'gtceu:maintenance_hatch[facing=east]', false)
      scene.world.setBlock(util.grid.at(2, 4, 2), 'gtceu:lv_muffler_hatch[facing=up]', false)

      // Layer 1: casing floor
      scene.world.showSection(util.select.layer(1), Direction.DOWN)
      scene.idle(15)
      scene.overlay.showText(70)
        .text('Bottom layer: Heatproof Machine Casings')
        .pointAt(util.vector.topOf(1, 1, 1))
        .placeNearTarget()
      scene.idle(80)
      scene.addKeyframe()

      gtcText(scene, util, 2, 1, 3, 'The controller goes in the front centre', 60)
      gtcText(scene, util, 1, 1, 3, 'Input Bus: ingots and dusts go in', 55)
      gtcText(scene, util, 3, 1, 3, 'Output Bus: finished ingots come out', 55)
      gtcText(scene, util, 1, 1, 2, 'Energy Hatch powers the furnace', 55)
      gtcText(scene, util, 3, 1, 2, 'Maintenance Hatch: keep it repaired', 55)
      scene.addKeyframe()

      // Coils
      scene.world.showSection(util.select.layer(2), Direction.DOWN)
      scene.idle(10)
      scene.world.showSection(util.select.layer(3), Direction.DOWN)
      scene.idle(15)
      scene.overlay.showText(70)
        .text('Two rings of Cupronickel Coils, hollow centre')
        .pointAt(util.vector.topOf(1, 3, 1))
        .placeNearTarget()
      scene.idle(80)
      gtcText(scene, util, 3, 3, 3, 'Coil tier sets the max temperature', 70)
      gtcText(scene, util, 3, 3, 1, 'Hotter coils unlock hotter recipes', 70)
      scene.addKeyframe()

      // Top
      scene.world.showSection(util.select.layer(4), Direction.DOWN)
      scene.idle(15)
      gtcText(scene, util, 2, 4, 2, 'Muffler Hatch on top; keep space above it', 70)

      scene.rotateCameraY(90)
      scene.idle(40)
      gtcNote(scene, 'Formed in-world when complete. Ponder may show it as invalid.', 80)
    })

  // ---------------------------------------------------------------- Steam setup
  event.create('gtceu:lp_steam_solid_boiler')
    .scene('gtc_steam_setup', 'Steam Power Setup', (scene, util) => {
      scene.configureBasePlate(0, 0, 6)
      scene.showBasePlate()
      scene.idle(10)

      gtcPut(scene, util, 1, 1, 2, 'gtceu:lp_steam_solid_boiler[facing=south]')
      gtcShow(scene, util, 1, 1, 2, 10)
      gtcText(scene, util, 1, 1, 2, 'Steam Boiler: burns coal or charcoal', 60)
      gtcNote(scene, 'It also needs water; fill it with a bucket or pipe', 70)
      scene.addKeyframe()

      gtcPut(scene, util, 2, 1, 2, 'gtceu:bronze_normal_fluid_pipe')
      gtcPut(scene, util, 3, 1, 2, 'gtceu:bronze_normal_fluid_pipe')
      gtcShow(scene, util, 2, 1, 2, 6)
      gtcShow(scene, util, 3, 1, 2, 10)
      gtcText(scene, util, 2, 1, 2, 'Bronze pipes carry steam to your machines', 65)

      gtcPut(scene, util, 4, 1, 2, 'gtceu:lp_steam_macerator[facing=south]')
      gtcShow(scene, util, 4, 1, 2, 10)
      gtcText(scene, util, 4, 1, 2, 'Steam Macerator: no cables needed', 60)
      scene.addKeyframe()

      gtcPut(scene, util, 4, 1, 3, 'gtceu:lp_steam_furnace[facing=south]')
      gtcShow(scene, util, 4, 1, 3, 10)
      gtcText(scene, util, 4, 1, 3, 'Steam Furnace works the same way', 55)

      gtcNote(scene, 'Steam leaves the boiler from its output side', 65)
      gtcNote(scene, 'Overheated or waterless boilers explode!', 65)
    })

  // ---------------------------------------------------------------- Power line
  event.create('gtceu:mv_transformer_1a')
    .scene('gtc_power_line', 'Power Line and Transformer', (scene, util) => {
      scene.configureBasePlate(0, 0, 7)
      scene.showBasePlate()
      scene.idle(10)

      gtcPut(scene, util, 1, 1, 3, 'gtceu:lv_steam_turbine[facing=east]')
      gtcShow(scene, util, 1, 1, 3, 10)
      gtcText(scene, util, 1, 1, 3, 'A generator produces power; this one is LV', 65)

      gtcPut(scene, util, 2, 1, 3, 'gtceu:tin_single_cable')
      gtcPut(scene, util, 3, 1, 3, 'gtceu:tin_single_cable')
      gtcShow(scene, util, 2, 1, 3, 6)
      gtcShow(scene, util, 3, 1, 3, 10)
      gtcText(scene, util, 2, 1, 3, 'Tin cables: LV, 32 V, 1 amp each', 65)
      scene.addKeyframe()

      gtcPut(scene, util, 4, 1, 3, 'gtceu:mv_transformer_1a[facing=east]')
      gtcShow(scene, util, 4, 1, 3, 10)
      gtcText(scene, util, 4, 1, 3, 'Transformer: steps LV up to MV (128 V)', 70)
      gtcNote(scene, 'Screwdriver the transformer to switch step-up or step-down', 80)
      scene.addKeyframe()

      gtcPut(scene, util, 5, 1, 3, 'gtceu:copper_single_cable')
      gtcShow(scene, util, 5, 1, 3, 6)
      gtcPut(scene, util, 5, 1, 4, 'gtceu:mv_macerator[facing=south]')
      gtcShow(scene, util, 5, 1, 4, 10)
      gtcText(scene, util, 5, 1, 3, 'Copper cable carries the MV side', 60)
      gtcText(scene, util, 5, 1, 4, 'An MV machine now runs at full speed', 65)
      scene.addKeyframe()

      gtcNote(scene, 'Voltage = tier. Amps = how many machines a cable can feed.', 80)
      gtcNote(scene, 'A cable over its amp limit burns out', 65)
      gtcNote(scene, 'A machine fed too much voltage explodes!', 70)
      scene.rotateCameraY(90)
      scene.idle(30)
    })

  // ---------------------------------------------------------------- Cleanroom
  event.create('gtceu:cleanroom')
    .scene('gtc_cleanroom', 'The Cleanroom', (scene, util) => {
      scene.configureBasePlate(0, 0, 7)
      scene.scaleSceneView(0.8)
      scene.showBasePlate()
      scene.idle(10)

      // Smallest valid cleanroom: 5x5 footprint, 5 tall (3x3x3 inside).
      // x1-5, z1-5, y1 = floor, y2-4 = walls, y5 = ceiling.
      for (let x = 1; x <= 5; x++) {
        for (let z = 1; z <= 5; z++) {
          const edge = (x === 1 || x === 5 || z === 1 || z === 5)
          scene.world.setBlock(util.grid.at(x, 1, z), 'gtceu:plascrete', false)
          for (let y = 2; y <= 4; y++) {
            if (edge) scene.world.setBlock(util.grid.at(x, y, z), 'gtceu:plascrete', false)
          }
          scene.world.setBlock(util.grid.at(x, 5, z), edge ? 'gtceu:plascrete' : 'gtceu:filter_casing', false)
        }
      }
      // Glass windows in the middle of the side walls
      scene.world.setBlock(util.grid.at(1, 3, 3), 'gtceu:cleanroom_glass', false)
      scene.world.setBlock(util.grid.at(5, 3, 3), 'gtceu:cleanroom_glass', false)
      scene.world.setBlock(util.grid.at(3, 3, 1), 'gtceu:cleanroom_glass', false)
      // Hatches and controller
      scene.world.setBlock(util.grid.at(3, 5, 5), 'gtceu:cleanroom[facing=south]', false)
      scene.world.setBlock(util.grid.at(1, 2, 2), 'gtceu:lv_energy_input_hatch[facing=west]', false)
      scene.world.setBlock(util.grid.at(5, 2, 2), 'gtceu:maintenance_hatch[facing=east]', false)

      scene.world.showSection(util.select.layer(1), Direction.DOWN)
      scene.idle(15)
      scene.overlay.showText(70)
        .text('Floor: a 5x5 square of Plascrete')
        .pointAt(util.vector.topOf(3, 1, 3))
        .placeNearTarget()
      scene.idle(80)
      scene.addKeyframe()

      scene.world.showSection(util.select.layers(2, 3), Direction.DOWN)
      scene.idle(10)
      scene.world.showSection(util.select.layer(4), Direction.DOWN)
      scene.idle(15)
      gtcText(scene, util, 1, 4, 1, 'Walls: Plascrete, 3 tall, hollow inside', 70)
      gtcText(scene, util, 5, 3, 3, 'Cleanroom Glass can replace wall blocks', 65)
      gtcText(scene, util, 1, 2, 2, 'An Energy Hatch powers the filters', 60)
      gtcText(scene, util, 5, 2, 2, 'Maintenance Hatch is required too', 60)
      scene.addKeyframe()

      scene.world.showSection(util.select.layer(5), Direction.DOWN)
      scene.idle(15)
      gtcText(scene, util, 3, 5, 3, 'Ceiling: Filter Casings over the interior', 70)
      gtcText(scene, util, 3, 5, 5, 'Controller sits in the ceiling edge', 65)
      scene.rotateCameraY(90)
      scene.idle(20)
      gtcNote(scene, 'Add a door in a wall so you can walk in', 65)
      gtcNote(scene, 'Machines inside get a clean environment', 65)
      gtcNote(scene, 'Required for nano circuits and other high-tech recipes', 80)
      gtcNote(scene, 'Formed in-world when complete. Ponder may show it as invalid.', 80)
    })

  // ---------------------------------------------------------------- Ore processing line
  event.create('gtceu:lv_ore_washer')
    .scene('gtc_ore_line', 'Ore Processing Line', (scene, util) => {
      scene.configureBasePlate(0, 0, 7)
      scene.showBasePlate()
      scene.idle(10)

      gtcPut(scene, util, 1, 1, 3, 'gtceu:lv_macerator[facing=south]')
      gtcShow(scene, util, 1, 1, 3, 10)
      gtcText(scene, util, 1, 1, 3, '1. Macerator: crushed ore, plus byproducts', 70)
      scene.addKeyframe()

      gtcPut(scene, util, 2, 1, 3, 'gtceu:lv_ore_washer[facing=south]')
      gtcShow(scene, util, 2, 1, 3, 10)
      gtcText(scene, util, 2, 1, 3, '2. Ore Washer: crushed to purified ore', 70)
      gtcNote(scene, 'It needs water, from a hatch or pipe', 65)
      scene.addKeyframe()

      gtcPut(scene, util, 3, 1, 3, 'gtceu:lv_thermal_centrifuge[facing=south]')
      gtcShow(scene, util, 3, 1, 3, 10)
      gtcText(scene, util, 3, 1, 3, '3. Thermal Centrifuge: purified to refined ore', 75)
      scene.addKeyframe()

      gtcPut(scene, util, 4, 1, 3, 'gtceu:lv_centrifuge[facing=south]')
      gtcShow(scene, util, 4, 1, 3, 10)
      gtcText(scene, util, 4, 1, 3, '4. Centrifuge: dust and rare byproduct dusts', 75)
      scene.addKeyframe()

      gtcNote(scene, 'Move items between machines by hand, hoppers or buses', 75)
      gtcNote(scene, 'Smelt the final dust, or EBF for alloys', 65)
      scene.rotateCameraY(90)
      scene.idle(30)
    })
})
