---
title: UTBLGameSingleton
type: class
aliases: UTBLGameSingleton
share: false

---

# UTBLGameSingleton





Inherits from UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| TArray< AActor * > | **[[GetActorsWithTag]]**(FName Tag, UWorld * World) const |
| void | **[[OnLevelAdded]]**(ULevel * Level, UWorld * World) |
| | **[[UTBLGameSingleton]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< UObject * > | **[[AsyncLoadedObjects]]**  |
| TArray< UObject * > | **[[CachedClassDefaultObjects]]**  |
| TMap< ECharacterClass, EOnlineStat > | **[[CharacterClassToStat]]**  |
| FSoftObjectPath | **[[CharacterCombatStatesClasssName]]**  |
| [UCharacterCustomizationSettings](/docs/SDK/Source/Classes/classUCharacterCustomizationSettings.md) * | **[[CharacterCustomizationSettings]]**  |
| TMap< FString, int32 > | **[[CharacterExertionSwitchEvents]]**  |
| UMaterial * | **[[CompositeMaterial]]**  |
| FSoftObjectPath | **[[CompositeMaterialName]]**  |
| UDataTable * | **[[CustomPersonalityEmotesDataTable]]**  |
| TArray< [FCustomPersonalityEmotesTableRow](/docs/SDK/Source/Classes/structFCustomPersonalityEmotesTableRow.md) > | **[[CustomPersonalityRows]]**  |
| TArray< [UCharacterCustomization](/docs/SDK/Source/Classes/classUCharacterCustomization.md) * > | **[[CustomizationPresets]]**  |
| TArray< [UDefaultCharacterCustomization](/docs/SDK/Source/Classes/classUDefaultCharacterCustomization.md) * > | **[[DefaultCharacterCustomizations]]**  |
| [UPlayerClassData](/docs/SDK/Source/Classes/classUPlayerClassData.md) * | **[[DefaultPlayerClassDataType]]**  |
| FSoftObjectPath | **[[DefaultPlayerClassDataTypeName]]**  |
| TArray< [UDefaultWeaponCustomization](/docs/SDK/Source/Classes/classUDefaultWeaponCustomization.md) * > | **[[DefaultWeaponsCustomizations]]**  |
| TArray< [FFactionOverridePersonalityEmoteTableRow](/docs/SDK/Source/Classes/structFFactionOverridePersonalityEmoteTableRow.md) > | **[[FactionOverridePersonalityEmotes]]**  |
| UDataTable * | **[[FactionOverridePersonalityEmotesDataTable]]**  |
| UMaterial * | **[[HeraldryRenderMaterial]]**  |
| FSoftObjectPath | **[[HeraldryRenderMaterialName]]**  |
| FSoftObjectPath | **[[HorseClassName]]**  |
| UClass * | **[[OnlineConfigClass]]**  |
| UDataTable * | **[[PersonalityEmotesDataTable]]**  |
| TArray< [FPersonalityEmoteTableRow](/docs/SDK/Source/Classes/structFPersonalityEmoteTableRow.md) > | **[[PersonalityRows]]**  |
| TMap< EOnlineStat, [UProgressionSpec](/docs/SDK/Source/Classes/classUProgressionSpec.md) * > | **[[ProgressionSpec]]**  |
| TMap< UWorld *, [UTextureAtlasManager](/docs/SDK/Source/Classes/classUTextureAtlasManager.md) * > | **[[TextureAtlasManagers]]**  |
| TMap< FString, int32 > | **[[WeaponActionSwitchEvents]]**  |
| FSoftObjectPath | **[[WeaponFistClassName]]**  |
| TMap< EWeaponTag, EOnlineStat > | **[[WeaponTagToStat]]**  |
| bool | **[[bNDAShown]]**  |
| bool | **[[bSynchronousLoad]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200