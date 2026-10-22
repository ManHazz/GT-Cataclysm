---
navigation:
  title: "LV Thermal Centrifuge"
  icon: gtceu:lv_thermal_centrifuge
  parent: ores.md
  position: 30
item_ids:
  - gtceu:lv_thermal_centrifuge
---

# LV Thermal Centrifuge

<ItemImage id="gtceu:lv_thermal_centrifuge" scale="4" />

The Thermal Centrifuge heats ore to turn it into refined ore. Tooltip: separating ores more precisely.

## What it does

Takes crushed or purified ore and outputs refined ore plus byproducts. Available in these tiers: LV, MV, HV, EV, IV, LuV, ZPM, UV.

## How to make it

<RecipeFor id="gtceu:lv_thermal_centrifuge" />

## What it makes and uses

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Thermal Centrifuge | Iron Purified Ore (any) | Refined Iron Ore, Tin Dust (33.33%) | 30 | 20 s |
| Thermal Centrifuge | Iron Crushed Ore (any) | Refined Iron Ore, Tin Dust (33.33%), Stone Dust | 30 | 20 s |

<ItemGrid>
  <ItemIcon id="gtceu:purified_iron_ore" />
  <ItemIcon id="gtceu:refined_iron_ore" />
  <ItemIcon id="gtceu:tin_dust" />
</ItemGrid>

## How it connects

<GameScene zoom="4" interactive={true}>
  <Block id="gtceu:lv_thermal_centrifuge" />
  <BlockAnnotation x="0" y="0" z="0">Power in on any side.</BlockAnnotation>
</GameScene>

## Tips

* Refined ore macerates to a dust with its own byproduct (table on [The Ore Chain](ore_chain.md)).
