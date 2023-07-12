---
title: UCinematicAnimationRemapping
type: class
aliases: UCinematicAnimationRemapping
share: false

---

# UCinematicAnimationRemapping





Inherits from UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| UAnimSequenceBase * | **[[OverrideSequencerAnimation]]**(UAnimSequenceBase * InAnim, USkeletalMeshComponent * SkelMeshComp) |
| | **[[UCinematicAnimationRemapping]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TMap< UAnimSequenceBase *, int32 > | **[[AnimToRemapSetsIndex]]**  |
| TArray< FString > | **[[AutomapWeaponNames]]**  |
| TArray< [FCinematicAnimationRemapSet](/docs/SDK/Source/Classes/structFCinematicAnimationRemapSet.md) > | **[[RemapSets]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200