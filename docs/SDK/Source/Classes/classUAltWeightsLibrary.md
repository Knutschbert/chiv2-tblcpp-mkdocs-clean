---
title: UAltWeightsLibrary
type: class
aliases: UAltWeightsLibrary
share: false

---

# UAltWeightsLibrary





Inherits from UBlueprintFunctionLibrary

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ClearAllSkinWeightsOverride]]**(USkinnedMeshComponent * InComp) |
| void | **[[InitPawnAltWeightsState]]**(ACharacter * Char) |
| bool | **[[InitSkinWeightsState]]**(USkinnedMeshComponent * InComp, UPARAM(Ref) [FAltWeightsState](/docs/SDK/Source/Classes/structFAltWeightsState.md) & InState) |
| bool | **[[SetSkinWeightsOverride]]**(USkinnedMeshComponent * InComp, const [FAltWeightsState](/docs/SDK/Source/Classes/structFAltWeightsState.md) & InState) |
| | **[[UAltWeightsLibrary]]**() |
| bool | **[[UpdateSkinWeightsOverride]]**(USkinnedMeshComponent * InComp, FName InBoneName, UPARAM(Ref) [FAltWeightsState](/docs/SDK/Source/Classes/structFAltWeightsState.md) & InOutState) |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200