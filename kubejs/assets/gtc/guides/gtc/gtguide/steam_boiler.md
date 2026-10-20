---
navigation:
  title: "Steam Boiler"
  icon: gtceu:lp_steam_solid_boiler
  parent: steam.md
  position: 10
item_ids:
  - gtceu:lp_steam_solid_boiler
  - gtceu:hp_steam_solid_boiler
  - gtceu:lp_steam_liquid_boiler
---

# Steam Boiler

<ItemImage id="gtceu:lp_steam_solid_boiler" scale="4" />

The Low Pressure Steam Solid Boiler burns solid fuel to turn water into steam. It is the usual first steam source.

## What it does

Solid boilers burn coal-type fuel to heat water. The GregTech Modern docs list base steam output as 6 mB/t for the Low Pressure Solid boiler and 15 mB/t for the High Pressure one. High Pressure versions unlock after steel.

## How to make it

<RecipeFor id="gtceu:lp_steam_solid_boiler" />

Press R in JEI on the boiler for the same recipe with item tags expanded.

## What it makes and uses

| Fuel | Burn time (ticks) |
|---|---|
| Coal | 1600 |
| Charcoal | 1600 |
| Coke Gem | 3200 |
| Coke Block | 28800 |

<ItemGrid>
  <ItemIcon id="minecraft:coal" />
  <ItemIcon id="minecraft:charcoal" />
  <ItemIcon id="gtceu:coke_gem" />
  <ItemIcon id="gtceu:coke_block" />
</ItemGrid>

Output: steam. Input: water (the docs suggest a Primitive Pump, or a water connection from another mod).

## How it connects

<GameScene zoom="4" interactive={true}>
  <ImportStructure src="structures/steam_setup.nbt" />
  <BlockAnnotation x="0" y="0" z="1">Low Pressure Steam Solid Boiler: fuel and water in, steam out.</BlockAnnotation>
  <BlockAnnotation x="2" y="0" z="1">Bronze fluid pipes carry the steam.</BlockAnnotation>
  <BlockAnnotation x="4" y="0" z="1">Low Pressure Steam Macerator: uses steam while it works.</BlockAnnotation>
</GameScene>

## Tips

* Do not pipe steam through wooden pipes: the game data marks wood and treated wood pipes as not gas-proof (tooltip: Gases may leak!).
* The docs warn that gas in a pipe that cannot contain it escapes and causes small explosions.
* Liquid boilers (for example the Low Pressure Steam Liquid Boiler) burn hot liquids instead of solid fuel; the docs give base output of 12 mB/t low pressure and 30 mB/t high pressure.
