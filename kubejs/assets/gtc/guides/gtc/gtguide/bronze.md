---
navigation:
  title: "Bronze"
  icon: gtceu:bronze_ingot
  parent: steam.md
  position: 30
item_ids:
  - gtceu:bronze_ingot
  - gtceu:bronze_dust
  - gtceu:lp_steam_alloy_smelter
---

# Bronze

<ItemImage id="gtceu:bronze_ingot" scale="4" />

Bronze is the key Steam Age material: three parts copper to one part tin.

## What it does

Bronze plates build the boilers, hulls and pipes of the Steam Age. The docs describe the first batch as: crush the ingots to dust with a GT mortar, mix them 3:1 in a crafting grid, then smelt the dust. A steam alloy smelter makes it faster and needs no mortar.

## How to make it

<RecipeFor id="gtceu:bronze_dust" />

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Mixer | 3x Copper Dust (any), Tin Dust (any), Programmed Circuit (config 1, not consumed) | 4x Bronze Dust | 7 | 20 s |
| Alloy Smelter | 3x Copper Dust (any), Tin Dust (any) | 4x Bronze Ingot | 16 | 10 s |

Smelting bronze dust in a furnace gives a bronze ingot (furnace recipe gtceu:smelting/smelt_dust_bronze_to_ingot).

## What it makes and uses

<ItemGrid>
  <ItemIcon id="gtceu:bronze_ingot" />
  <ItemIcon id="gtceu:bronze_dust" />
  <ItemIcon id="gtceu:bronze_machine_casing" />
  <ItemIcon id="gtceu:bronze_normal_fluid_pipe" />
  <ItemIcon id="gtceu:lp_steam_solid_boiler" />
</ItemGrid>

Bronze is used in the [boiler](steam_boiler.md), the [pipes](fluid_pipes.md) and the [hulls](steam_hulls.md).

## How it connects

<GameScene zoom="4" interactive={true}>
  <Block id="gtceu:lp_steam_alloy_smelter" />
  <BlockAnnotation x="0" y="0" z="0">Low Pressure Steam Alloy Smelter: copper and tin in, bronze out. Runs on steam.</BlockAnnotation>
</GameScene>

## Tips

* Crafting 3 copper dust + 1 tin dust gives 3 bronze dust; the Mixer and Alloy Smelter give 4 per batch (see tables).
