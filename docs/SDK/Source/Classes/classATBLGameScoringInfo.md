---
title: ATBLGameScoringInfo
type: class
aliases: ATBLGameScoringInfo
share: false

---

# ATBLGameScoringInfo





Inherits from AInfo

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ATBLGameScoringInfo]]**() |
| void | **[[OnHorseKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & DamageEvent) |
| void | **[[PawnDowned]]**(APawn * DownedPlayer, AActor * DamageCauser, [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * DamageSource) |
| void | **[[PawnRevived]]**(APawn * RevivedPlayer, APawn * RevivorPlayer) |
| void | **[[PlayerKilled]]**(AController * Killer, AController * Killed, [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * DamageSource, [FDeathEvent](/docs/SDK/Source/Classes/structFDeathEvent.md) DeathEvent, const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & DamageEvent) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| UDataTable * | **[[GameScoringDataTable]]**  |
| UCurveFloat * | **[[LongshotCurve]]**  |
| UDataTable * | **[[TeamScoreFormatDataTable]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200