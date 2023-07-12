---
title: UGoreFXLibrary
type: class
aliases: UGoreFXLibrary
share: false

---

# UGoreFXLibrary





Inherits from UBlueprintFunctionLibrary

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[BreakAtBone]]**(ACharacter * Char, FName BoneName, const FVector & Impulse, const FVector & HitLocation, bool bSpawnedItem) |
| void | **[[FillUpComponentSpaceTransformsRefPose]]**(const USkeletalMeshComponent * SKM, TArray< FTransform > & ComponentSpaceTransforms) |
| FName | **[[FindClosestBoneFromGiven]]**(const USkinnedMeshComponent * InSkinnedMesh, const [UBoneList](/docs/SDK/Source/Classes/classUBoneList.md) * InBreakableBones, const FVector & InTestLocation, FVector & OutBoneLocation, float & OutClosestDistance) |
| bool | **[[GetGoreActionFromAttack]]**(const [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * InIventoryItem, FName InAttackName, [FWeaponGoreSlot](/docs/SDK/Source/Classes/structFWeaponGoreSlot.md) & GoreAction) |
| USkeletalMeshComponent * | **[[KnockoffHelmet]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Char) |
| | **[[UGoreFXLibrary]]**() |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200