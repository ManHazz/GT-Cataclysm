---
navigation:
  title: "LV Wiremill"
  icon: gtceu:lv_wiremill
  parent: machines.md
  position: 50
item_ids:
  - gtceu:lv_wiremill
---

# LV Wiremill

<ItemImage id="gtceu:lv_wiremill" scale="4" />

The Wiremill draws ingots into wire.

## What it does

The programmed circuit in the recipe picks the wire size: config 1 gives single wire, config 3 fine wire, config 16 hex wire (recipes below).

Available in these tiers: LV, MV, HV, EV, IV, LuV, ZPM, UV. Details of the electric rules: [Amperage and overload](amperage.md).

## How to make it

<RecipeFor id="gtceu:lv_wiremill" />

## What it makes and uses

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Wiremill | Nickel Ingot (any), Programmed Circuit (config 1, not consumed) | 2x Nickel Single Wire | 7 | 2.9 s |
| Wiremill | Tin Ingot (any), Programmed Circuit (config 3, not consumed) | 8x Fine Tin Wire | 7 | 17.7 s |
| Wiremill | 8x Copper Ingot (any), Programmed Circuit (config 16, not consumed) | Copper Hex Wire | 7 | 25.2 s |

<ItemGrid>
  <ItemIcon id="gtceu:nickel_single_wire" />
  <ItemIcon id="gtceu:fine_tin_wire" />
  <ItemIcon id="gtceu:copper_hex_wire" />
  <ItemIcon id="gtceu:programmed_circuit" />
</ItemGrid>

## How it connects

<GameScene zoom="4" interactive={true}>
  <Block id="gtceu:lv_wiremill" />
  <BlockAnnotation x="0" y="0" z="0">Power in on any side.</BlockAnnotation>
</GameScene>

## Tips

* Wire plus insulation becomes cable: see [Cables](cables.md).
