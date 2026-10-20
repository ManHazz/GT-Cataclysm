---
navigation:
  title: "Generators"
  icon: gtceu:lv_combustion
  parent: power.md
  position: 20
item_ids:
  - gtceu:lv_combustion
  - gtceu:lv_steam_turbine
  - gtceu:lv_gas_turbine
---

# Generators

<ItemImage id="gtceu:lv_combustion" scale="4" />

Single-block generators burn liquid or gas fuel and output EU from one side.

## What it does

From LV to HV, EU comes from single-block generators. They consume liquid or gas fuel (no items), and output exactly 1 amp at their tier voltage from one marked output side (docs). The Basic Combustion Generator burns flammable liquids, the Gas Turbine burns flammable gases, and the Steam Turbine converts steam (tooltips). MV and HV versions burn more fuel per tick to reach their higher voltage (docs). At EV and above generation moves to multiblocks.

## How to make it

<RecipeFor id="gtceu:lv_combustion" />

<RecipeFor id="gtceu:lv_steam_turbine" />

<RecipeFor id="gtceu:lv_gas_turbine" />

## What it makes and uses

| Fuel | EU/t produced | Burn time (ticks) |
|---|---|---|
| 1 mB Diesel | 32 | 15 |
| 2 mB Methane | 32 | 7 |
| 640 mB Steam | 32 | 10 |

The table shows the LV-tier fuel rate of each type from the recipe data; JEI lists every valid fuel.

<ItemGrid>
  <ItemIcon id="gtceu:lv_combustion" />
  <ItemIcon id="gtceu:lv_steam_turbine" />
  <ItemIcon id="gtceu:lv_gas_turbine" />
  <ItemIcon id="gtceu:mv_combustion" />
</ItemGrid>

## How it connects

<GameScene zoom="4" interactive={true}>
  <Block id="gtceu:lv_combustion" />
  <BlockAnnotation x="0" y="0" z="0">Fuel liquid in. EU out of the marked output side as 1A at 32 V.</BlockAnnotation>
</GameScene>

## Tips

* Generators cannot be placed inside a Cleanroom; it blocks the cleanroom controller (docs and tooltip).
* A single generator is 1A. A machine that wants more than 1A is fed by a battery buffer or several generators: see [Batteries and Buffers](batteries.md).
