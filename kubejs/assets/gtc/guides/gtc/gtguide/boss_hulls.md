---
navigation:
  title: "Boss-Gated Hulls"
  icon: gtceu:mv_machine_hull
  parent: pack.md
  position: 10
item_ids:
  - gtceu:mv_machine_hull
  - gtceu:hv_machine_hull
  - gtceu:ev_machine_hull
  - gtceu:iv_machine_hull
  - gtceu:luv_machine_hull
  - gtceu:zpm_machine_hull
  - cataclysm:monstrous_horn
  - cataclysm:ignitium_ingot
  - cataclysm:witherite_ingot
  - cataclysm:gauntlet_of_guard
  - cataclysm:cursium_ingot
  - cataclysm:essence_of_the_storm
---

# Boss-Gated Hulls

<ItemImage id="gtceu:mv_machine_hull" scale="4" />

In GT-Cataclysm every machine hull from MV up needs a drop from a Cataclysm boss. No boss drop, no hull, no machines of that tier.

## What it does

The pack removes every recipe that outputs these hulls (including the crafting-table route) and adds one Assembler recipe per hull. The boss drop sits in the recipe as a catalyst that is not consumed, so one drop unlocks that tier for good. Source: kubejs/server_scripts/gating/.

| Hull tier | Boss | Drop (not consumed) | Cable | Fluid (288 mB) |
|---|---|---|---|---|
| MV | Netherite Monstrosity | Monstrous Horn | Copper or Annealed Copper | Polyethylene |
| HV | Ignis | Ignitium Ingot | Gold | Polyethylene |
| EV | The Harbinger | Witherite Ingot | Aluminium | Polyethylene |
| IV | Ender Guardian | Gauntlet Of Guard | Platinum | Polytetrafluoroethylene |
| LuV | Maledictus | Cursium Ingot | Niobium Titanium | Polytetrafluoroethylene |
| ZPM | Scylla | Essence Of The Storm | Vanadium Gallium | Polybenzimidazole |

LV and ULV hulls are untouched.

## How to make it

See [The Gated Hull Recipe](hull_recipe.md).

## What it makes and uses

<ItemGrid>
  <ItemIcon id="gtceu:mv_machine_hull" />
  <ItemIcon id="gtceu:hv_machine_hull" />
  <ItemIcon id="gtceu:ev_machine_hull" />
  <ItemIcon id="gtceu:iv_machine_hull" />
  <ItemIcon id="gtceu:luv_machine_hull" />
  <ItemIcon id="gtceu:zpm_machine_hull" />
</ItemGrid>

<ItemGrid>
  <ItemIcon id="cataclysm:monstrous_horn" />
  <ItemIcon id="cataclysm:ignitium_ingot" />
  <ItemIcon id="cataclysm:witherite_ingot" />
  <ItemIcon id="cataclysm:gauntlet_of_guard" />
  <ItemIcon id="cataclysm:cursium_ingot" />
  <ItemIcon id="cataclysm:essence_of_the_storm" />
</ItemGrid>

Everything built from a hull follows: for example the MV Macerator, the Pyrolyse Oven (MV hull), the Cleanroom (HV hull) and the Assembly Line (IV hull) all list the hull in their recipes.

## How it connects

<GameScene zoom="4" interactive={true}>
  <Block id="gtceu:mv_machine_hull" />
  <BlockAnnotation x="0" y="0" z="0">MV Machine Hull: needs the Netherite Monstrosity drop.</BlockAnnotation>
</GameScene>

## Tips

* Hull gates only touch the hull recipe. Casings, cables and fluids keep their normal recipes.
* Boss order in the pack: MV Netherite Monstrosity, HV Ignis, EV The Harbinger, IV Ender Guardian, LuV Maledictus, ZPM Scylla.
