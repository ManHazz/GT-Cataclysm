---
navigation:
  title: "The Gated Hull Recipe"
  icon: gtceu:lv_assembler
  parent: pack.md
  position: 20
item_ids:
  - gtceu:lv_machine_casing
  - gtceu:mv_machine_casing
  - gtceu:lv_assembler
---

# The Gated Hull Recipe

<ItemImage id="gtceu:mv_machine_casing" scale="4" />

How a gated hull is built in the Assembler.

## What it does

Each gated hull recipe is an Assembler recipe: one machine casing of that tier + 2 cables of the tier's cable type, with the boss drop as a non-consumed input, plus 288 mB of the tier's plastic. It takes 50 ticks (2.5 s) at 16 EU/t. The MV recipe exists once for copper cable and once for annealed copper cable.

## How to make it

Example (LV hull, for comparison, from the game):

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Assembler | LV Machine Casing, 2x Tin Single Cable, 288 mB Polyethylene | LV Machine Hull | 16 | 2.5 s |

MV hull in this pack: MV Machine Casing + 2 Copper Cable (or Annealed Copper Cable) + Monstrous Horn (not consumed) + 288 mB Polyethylene.

## What it makes and uses

| Hull tier | Boss | Drop (not consumed) | Cable | Fluid (288 mB) |
|---|---|---|---|---|
| MV | Netherite Monstrosity | Monstrous Horn | Copper or Annealed Copper | Polyethylene |
| HV | Ignis | Ignitium Ingot | Gold | Polyethylene |
| EV | The Harbinger | Witherite Ingot | Aluminium | Polyethylene |
| IV | Ender Guardian | Gauntlet Of Guard | Platinum | Polytetrafluoroethylene |
| LuV | Maledictus | Cursium Ingot | Niobium Titanium | Polytetrafluoroethylene |
| ZPM | Scylla | Essence Of The Storm | Vanadium Gallium | Polybenzimidazole |

<ItemGrid>
  <ItemIcon id="gtceu:mv_machine_casing" />
  <ItemIcon id="gtceu:hv_machine_casing" />
  <ItemIcon id="gtceu:ev_machine_casing" />
  <ItemIcon id="gtceu:iv_machine_casing" />
  <ItemIcon id="gtceu:luv_machine_casing" />
  <ItemIcon id="gtceu:zpm_machine_casing" />
</ItemGrid>

## How it connects

<GameScene zoom="4" interactive={true}>
  <Block id="gtceu:lv_assembler" />
  <BlockAnnotation x="0" y="0" z="0">The hull recipe runs in an Assembler.</BlockAnnotation>
</GameScene>

## Tips

* All gated hulls use the same numbers in the scripts: 50 ticks at 16 EU/t.
* Machine casing recipes are not touched by the gate, so casings can be stocked before the boss falls.
