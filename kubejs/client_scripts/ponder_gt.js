// PonderJS 2.x (Ponder 1.0.92): Ponder.registry fires client-side.
Ponder.registry(event => {
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
})
