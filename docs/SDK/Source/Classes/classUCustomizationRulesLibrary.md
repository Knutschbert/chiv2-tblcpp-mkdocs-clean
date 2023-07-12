---
title: UCustomizationRulesLibrary
type: class
aliases: UCustomizationRulesLibrary
share: false

---

# UCustomizationRulesLibrary





Inherits from UBlueprintFunctionLibrary

## Public Functions

|                | Name           |
| -------------- | -------------- |
| TArray< FPrimaryAssetId > | **[[FilterCustomizationAssets]]**(const TArray< FPrimaryAssetId > & CustomizationAssets, const [FCustomizationConstraintsQuery](/docs/SDK/Source/Classes/structFCustomizationConstraintsQuery.md) & ConstraintsQuery) |
| TArray< [FCustomizationEntry](/docs/SDK/Source/Classes/structFCustomizationEntry.md) > | **[[FilterCustomizationEntries]]**(const TArray< [FCustomizationEntry](/docs/SDK/Source/Classes/structFCustomizationEntry.md) > & CustomizationEntries, const [FCustomizationConstraintsQuery](/docs/SDK/Source/Classes/structFCustomizationConstraintsQuery.md) & ConstraintsQuery) |
| FPrimaryAssetId | **[[FindReplacementAsset]]**(const FPrimaryAssetId & AssetToReplace, TEnumAsByte< EAudioClassType::Type > ClassType, EFaction Faction, const [FCustomizationConstraintsQuery](/docs/SDK/Source/Classes/structFCustomizationConstraintsQuery.md) & ConstraintsQuery, const [FCustomizationCompatibilityQuery](/docs/SDK/Source/Classes/structFCustomizationCompatibilityQuery.md) & CompatibilityQuery, const [FCustomizationConstraintsQuery](/docs/SDK/Source/Classes/structFCustomizationConstraintsQuery.md) & OptionalConstraintsQuery, const [FCustomizationCompatibilityQuery](/docs/SDK/Source/Classes/structFCustomizationCompatibilityQuery.md) & OptionalCompatibilityQuery, int32 Alignment, const TArray< FPrimaryAssetId > & DefaultAssets) |
| void | **[[GroupCustomizationEntries]]**([ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * PlayerController, const TArray< [FCustomizationEntry](/docs/SDK/Source/Classes/structFCustomizationEntry.md) > & CustomizationEntries, TArray< [FCustomizationEntriesGroup](/docs/SDK/Source/Classes/structFCustomizationEntriesGroup.md) > & CustomizationGroups, ECustomizationGroupSearchResult & SearchResult) |
| TArray< FPrimaryAssetId > | **[[OnlyCustomizationAssetsCompatibleWithOwnerPreset]]**([ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * PlayerController, const TArray< FPrimaryAssetId > & CustomizationAssets, TEnumAsByte< EAudioClassType::Type > ClassType, EFaction Faction) |
| TArray< [FCustomizationEntry](/docs/SDK/Source/Classes/structFCustomizationEntry.md) > | **[[OnlyCustomizationEntriesCompatibleWithOwnerPreset]]**([ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * PlayerController, const TArray< [FCustomizationEntry](/docs/SDK/Source/Classes/structFCustomizationEntry.md) > & CustomizationEntries, TEnumAsByte< EAudioClassType::Type > ClassType, EFaction Faction) |
| void | **[[SortCustomizationEntries]]**(UPARAM(Ref) TArray< [FCustomizationEntry](/docs/SDK/Source/Classes/structFCustomizationEntry.md) > & RefCustomizationEntries, bool bSortByLevel, bool bSortByAlignment, bool bSortByRarity) |
| | **[[UCustomizationRulesLibrary]]**() |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200