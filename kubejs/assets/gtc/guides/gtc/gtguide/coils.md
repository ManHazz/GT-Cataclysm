---
navigation:
  title: "Heating Coils"
  icon: gtceu:cupronickel_coil_block
  parent: multiblocks.md
  position: 20
item_ids:
  - gtceu:cupronickel_coil_block
  - gtceu:kanthal_coil_block
  - gtceu:nichrome_coil_block
  - gtceu:rtm_alloy_coil_block
  - gtceu:hssg_coil_block
  - gtceu:naquadah_coil_block
  - gtceu:trinium_coil_block
  - gtceu:tritanium_coil_block
---

# Heating Coils

<ItemImage id="gtceu:cupronickel_coil_block" scale="4" />

Coils set how hot an EBF can get and how fast a Pyrolyse Oven runs.

## What it does

Heating coils come in tiers. Their Base Heat Capacity decides which EBF recipes you can run (each recipe lists a required temperature). All coils in one multiblock must be the same type.

## How to make it

| Machine | Input | Output | EU/t | Time |
|---|---|---|---|---|
| Assembler | 8x Cupronickel Double Wire, 8x Bronze Foil (any), 144 mB Tin Alloy | Cupronickel Coil Block | 30 | 10 s |
| Assembler | 8x Kanthal Double Wire, 8x Aluminium Foil (any), 144 mB Copper | Kanthal Coil Block | 120 | 15 s |

## What it makes and uses

| Coil block | Base heat capacity |
|---|---|
| Cupronickel | 1800 K |
| Kanthal | 2700 K |
| Nichrome | 3600 K |
| Rtm Alloy | 4500 K |
| Hssg | 5400 K |
| Naquadah | 7200 K |
| Trinium | 9001 K |
| Tritanium | 10800 K |

<ItemGrid>
  <ItemIcon id="gtceu:cupronickel_coil_block" />
  <ItemIcon id="gtceu:kanthal_coil_block" />
  <ItemIcon id="gtceu:nichrome_coil_block" />
  <ItemIcon id="gtceu:rtm_alloy_coil_block" />
  <ItemIcon id="gtceu:hssg_coil_block" />
  <ItemIcon id="gtceu:naquadah_coil_block" />
  <ItemIcon id="gtceu:trinium_coil_block" />
  <ItemIcon id="gtceu:tritanium_coil_block" />
</ItemGrid>

Pyrolyse Oven (tooltip): Cupronickel coils are 25% slower; every coil after Kanthal increases speed by 50%.

## How it connects

<GameScene zoom="3" interactive={true}>
  <ImportStructure src="structures/ebf.nbt" />
  <BoxAnnotation min="0 1 0" max="3 3 3" color="#ff7733">Heating coils: two rings of eight.</BoxAnnotation>
</GameScene>

## Tips

* Higher voltage adds heat: +100 K per voltage tier above MV (EBF tooltip).
* The coil data on this page was read from the game: Cupronickel 1800 K, Kanthal 2700 K, Nichrome 3600 K, RTM Alloy 4500 K, HSS-G 5400 K, Naquadah 7200 K, Trinium 9001 K, Tritanium 10800 K.
