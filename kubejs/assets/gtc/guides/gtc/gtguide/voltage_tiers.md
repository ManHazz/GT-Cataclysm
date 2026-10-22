---
navigation:
  title: "Voltage Tiers"
  icon: gtceu:lv_machine_hull
  parent: power.md
  position: 10
item_ids:
  - gtceu:ulv_machine_hull
  - gtceu:lv_machine_hull
  - gtceu:mv_machine_hull
  - gtceu:hv_machine_hull
  - gtceu:ev_machine_hull
  - gtceu:iv_machine_hull
---

# Voltage Tiers

<ItemImage id="gtceu:lv_machine_hull" scale="4" />

Every machine, cable and generator has a voltage tier. Each tier is four times the voltage of the one before.

## What it does

Voltage (V) is the size of one energy packet; amperage (A) is how many packets move at once. Voltage x amperage = EU/t, and EU/t x time = total EU (docs). Tiers in order: ULV, LV, MV, HV, EV, IV, LuV, ZPM, UV, UHV, UEV, UIV, UXV, OpV, MAX.

## How to make it

Each tier's machine hull is the base of every machine of that tier. LV is crafted:

<RecipeFor id="gtceu:lv_machine_hull" />

From MV upward the hull recipes are replaced in this pack: see [Pack: boss-gated hulls](pack.md).

## What it makes and uses

| Tier | Voltage | Example cable (max voltage from game data) |
|---|---|---|
| ULV | 8 | Lead cable (8 V) |
| LV | 32 | Tin cable (32 V) |
| MV | 128 | Copper cable (128 V) |
| HV | 512 | Gold cable (512 V) |
| EV | 2048 | Aluminium cable (2048 V) |
| IV | 8192 | Platinum cable (8192 V) |

<ItemGrid>
  <ItemIcon id="gtceu:ulv_machine_hull" />
  <ItemIcon id="gtceu:lv_machine_hull" />
  <ItemIcon id="gtceu:mv_machine_hull" />
  <ItemIcon id="gtceu:hv_machine_hull" />
  <ItemIcon id="gtceu:ev_machine_hull" />
  <ItemIcon id="gtceu:iv_machine_hull" />
</ItemGrid>

## How it connects

<GameScene zoom="4" interactive={true}>
  <Block id="gtceu:lv_machine_hull" />
  <BlockAnnotation x="0" y="0" z="0">LV Machine Hull: the 32 V base of every LV machine.</BlockAnnotation>
</GameScene>

## Tips

* A machine fed a voltage above its tier explodes (docs). See [Amperage and overload](amperage.md).
* Transformers step between adjacent tiers: [Transformers and Diodes](transformers.md).
