---
title: UMapOptionsObject
type: class
aliases: UMapOptionsObject
share: false

---

# UMapOptionsObject





Inherits from UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| FString | **[[GenerateMapURL]]**(TArray< [UMapModifierProperty](/docs/SDK/Source/Classes/classUMapModifierProperty.md) * > InMapModifierProperties) |
| FText | **[[GetGameModeMapName]]**(TEnumAsByte< EGameModeType::Type > GamemodeType) |
| bool | **[[GetMapMofidiersForGameMode]]**(TEnumAsByte< EGameModeType::Type > GamemodeType, TArray< [UMapModifierProperty](/docs/SDK/Source/Classes/classUMapModifierProperty.md) * > & MapModifiers) const |
| | **[[UMapOptionsObject]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< TEnumAsByte< EGameModeType::Type > > | **[[GameModeTypes]]**  |
| [UMapModifierComboBoxProperty](/docs/SDK/Source/Classes/classUMapModifierComboBoxProperty.md) * | **[[GamemodeTypesComboboxProperty]]**  |
| FText | **[[MapName]]**  |
| TMap< TEnumAsByte< EGameModeType::Type >, FText > | **[[MapNameByGameMode]]**  |
| TMap< TEnumAsByte< EGameModeType::Type >, [FMapModifierPropertiesArray](/docs/SDK/Source/Classes/structFMapModifierPropertiesArray.md) > | **[[MapPropertiesByGameModeType]]**  |
| [UMapModifierComboBoxProperty](/docs/SDK/Source/Classes/classUMapModifierComboBoxProperty.md) * | **[[ServerTypeComboboxProperty]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200