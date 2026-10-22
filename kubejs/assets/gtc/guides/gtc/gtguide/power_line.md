---
navigation:
  title: "Power Line Example"
  icon: gtceu:lv_transformer_1a
  parent: power.md
  position: 70
item_ids:
  - gtceu:mv_combustion
  - gtceu:copper_single_cable
  - gtceu:lv_transformer_1a
  - gtceu:tin_quadruple_cable
  - gtceu:lv_macerator
---

# Power Line Example

<ItemImage id="gtceu:lv_transformer_1a" scale="4" />

A complete chain: generator, cable, transformer, cable, machine.

## What it does

An MV Combustion Generator makes 1 amp at 128 V. Copper cable (max 128 V, 1 amp, from the game data) carries it to an LV Transformer, which by default steps DOWN: 1A MV in, 4A LV out. Quadruple tin cable (max 32 V, 4 amps with 4x the single 1A rating) carries that LV power to an LV Macerator.

## How to make it

Craft each part from its own page:

* <ItemLink id="gtceu:mv_combustion" />
* <ItemLink id="gtceu:copper_single_cable" />
* <ItemLink id="gtceu:lv_transformer_1a" />
* <ItemLink id="gtceu:tin_quadruple_cable" />
* <ItemLink id="gtceu:lv_macerator" />

## What it makes and uses

Result: the LV macerator can draw up to 4A at 32 V from one 128 V generator, instead of needing four LV generators.

## How it connects

<GameScene zoom="3" interactive={true}>
  <ImportStructure src="structures/power_line.nbt" />
  <BlockAnnotation x="0" y="0" z="1">MV Combustion Generator (1A @ 128 V)</BlockAnnotation>
  <BoxAnnotation min="1 0 1" max="3 1 2" color="#ffaa33">Copper cable: MV side</BoxAnnotation>
  <BlockAnnotation x="3" y="0" z="1">LV Transformer (Transform Down)</BlockAnnotation>
  <BoxAnnotation min="4 0 1" max="6 1 2" color="#aaaaaa">4x tin cable: LV side, 4 amps</BoxAnnotation>
  <BlockAnnotation x="6" y="0" z="1">LV Macerator</BlockAnnotation>
</GameScene>

## Tips

* The scene shows the layout only. Cable sides must be connected with Wire Cutters if they did not auto-connect when placing.
* Check the colored output dot on the generator and transformer before connecting (docs: EU leaves a block only from its output side).
