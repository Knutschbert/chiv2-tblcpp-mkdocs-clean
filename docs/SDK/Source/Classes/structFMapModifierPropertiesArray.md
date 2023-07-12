---
title: FMapModifierPropertiesArray
type: struct
aliases: FMapModifierPropertiesArray
share: false

---

# FMapModifierPropertiesArray





## Public Functions

|                | Name           |
| -------------- | -------------- |
| TBL_API | **[[FMapModifierPropertiesArray]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TMap< EHardwarePlatform, [FMapBotData](/docs/SDK/Source/Classes/structFMapBotData.md) > | **[[BotCounts]]**  |
| TEnumAsByte< EGameModeType::Type > | **[[GamemodeType]]**  |
| FString | **[[MapAssetStr]]**  |
| TArray< [FModifierPropertyOverride](/docs/SDK/Source/Classes/structFModifierPropertyOverride.md) > | **[[MapModifierOverrides]]**  |
| TArray< [UMapModifierProperty](/docs/SDK/Source/Classes/classUMapModifierProperty.md) * > | **[[MapModifierProperties]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:01 +0200