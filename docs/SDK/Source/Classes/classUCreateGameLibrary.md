---
title: UCreateGameLibrary
type: class
aliases: UCreateGameLibrary
share: false

---

# UCreateGameLibrary





Inherits from UBlueprintFunctionLibrary

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[GetDefaultModifiersForGameMode]]**(TEnumAsByte< EGameModeType::Type > GameMode, TArray< [UMapModifierProperty](/docs/SDK/Source/Classes/classUMapModifierProperty.md) * > & Modifiers) |
| void | **[[GetFFAOptions]]**(UObject * WorldContextObject, int32 & ScoreLimitOverride, int32 & TimeLimitOverride) |
| bool | **[[GetGenericModifiers]]**(TArray< [UMapModifierProperty](/docs/SDK/Source/Classes/classUMapModifierProperty.md) * > & Modifiers) |
| int32 | **[[GetGlobalTimeLimitOverride]]**() |
| void | **[[GetTDMOptions]]**(UObject * WorldContextObject, int32 & TicketCountOverride, int32 & TimeLimitOverride) |
| void | **[[GetTOOptions]]**(UObject * WorldContextObject, int32 & ThereAreNoOptionsAtTheMoment) |
| [UMapOptionsObject](/docs/SDK/Source/Classes/classUMapOptionsObject.md) * | **[[MakeMapOption]]**(UObject * WorldContextObject, [FMapOption](/docs/SDK/Source/Classes/structFMapOption.md) MapOptions) |
| | **[[UCreateGameLibrary]]**() |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200