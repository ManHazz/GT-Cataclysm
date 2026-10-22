---
navigation:
  title: "LV Bender"
  icon: gtceu:lv_bender
  parent: machines.md
  position: 60
item_ids:
  - gtceu:lv_bender
---

# LV Bender

<ItemImage id="gtceu:lv_bender" scale="4" />

The Bender presses ingots and plates into plates, double plates and foils.

## What it does

The programmed circuit chooses the shape: config 1 plate, config 2 double plate, config 10 foil (recipes below).

Available in these tiers: LV, MV, HV, EV, IV, LuV, ZPM, UV. Details of the electric rules: [Amperage and overload](amperage.md).

## How to make it

<RecipeFor id="gtceu:lv_bender" />

## What it makes and uses

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Bender | Programmed Circuit (config 1, not consumed), Cobalt Ingot (any) | Cobalt Plate | 24 | 2.95 s |
| Bender | 2x Tin Ingot (any), Programmed Circuit (config 2, not consumed) | Double Tin Plate | 96 | 11.8 s |
| Bender | Bronze Ingot (any), Programmed Circuit (config 10, not consumed) | 4x Bronze Foil | 24 | 3.8 s |

<ItemGrid>
  <ItemIcon id="gtceu:cobalt_plate" />
  <ItemIcon id="gtceu:double_tin_plate" />
  <ItemIcon id="gtceu:bronze_foil" />
  <ItemIcon id="gtceu:programmed_circuit" />
</ItemGrid>

## How it connects

<GameScene zoom="4" interactive={true}>
  <Block id="gtceu:lv_bender" />
  <BlockAnnotation x="0" y="0" z="0">Power in on any side.</BlockAnnotation>
</GameScene>

## Tips

* The LV Bender recipe itself needs steel plates.
