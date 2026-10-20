---
navigation:
  title: "LV Ore Washer"
  icon: gtceu:lv_ore_washer
  parent: machines.md
  position: 120
item_ids:
  - gtceu:lv_ore_washer
---

# LV Ore Washer

<ItemImage id="gtceu:lv_ore_washer" scale="4" />

The Ore Washer cleans crushed ore into purified ore with water.

## What it does

Crushed ore plus water becomes purified ore plus byproducts. Different programmed circuits and distilled water change speed and byproducts (recipes below).

Available in these tiers: LV, MV, HV, EV, IV, LuV, ZPM, UV. Details of the electric rules: [Amperage and overload](amperage.md).

## How to make it

<RecipeFor id="gtceu:lv_ore_washer" />

## What it makes and uses

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Ore Washer | Iron Crushed Ore (any), Programmed Circuit (config 1, not consumed), 1000 mB Water | Purified Iron Ore, Nickel Dust (33.33%), Stone Dust | 16 | 20 s |
| Ore Washer | Iron Crushed Ore (any), 100 mB Distilled Water | Purified Iron Ore, Nickel Dust (33.33%), Stone Dust | 16 | 10 s |
| Ore Washer | Iron Crushed Ore (any), Programmed Circuit (config 2, not consumed), 100 mB Water | Purified Iron Ore | 4 | 0.4 s |
| Ore Washer | Iron Impure Dust (any), Programmed Circuit (config 2, not consumed), 100 mB Water | Iron Dust | 4 | 0.4 s |

<ItemGrid>
  <ItemIcon id="gtceu:crushed_iron_ore" />
  <ItemIcon id="gtceu:purified_iron_ore" />
  <ItemIcon id="gtceu:impure_iron_dust" />
  <ItemIcon id="gtceu:iron_dust" />
</ItemGrid>

## How it connects

<GameScene zoom="4" interactive={true}>
  <Block id="gtceu:lv_ore_washer" />
  <BlockAnnotation x="0" y="0" z="0">Power in on any side. Needs water.</BlockAnnotation>
</GameScene>

## Tips

* The config 1 recipe takes 20 s with byproducts; the config 2 recipe takes under half a second and gives no byproduct.
