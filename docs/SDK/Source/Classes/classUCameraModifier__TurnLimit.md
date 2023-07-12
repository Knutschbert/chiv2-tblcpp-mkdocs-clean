---
title: UCameraModifier_TurnLimit
type: class
aliases: UCameraModifier_TurnLimit
share: false

---

# UCameraModifier_TurnLimit





Inherits from UCameraModifier

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UCameraModifier_TurnLimit]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| float | **[[CalcTurnLimit]]**(float InPercent) |
| void | **[[SmoothTurnLimitEnding]]**(float & CurrentTurnLimit, float & EndSpeed, float TargetTurnLimit, float DeltaTime) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[DownTurnLimit]]**  |
| float | **[[DownTurnRatePercent]]**  |
| float | **[[LeftTurnLimit]]**  |
| float | **[[LeftTurnRatePercent]]**  |
| float | **[[RightTurnLimit]]**  |
| float | **[[RightTurnRatePercent]]**  |
| float | **[[UpTurnLimit]]**  |
| float | **[[UpTurnRatePercent]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[DownTurnRateEndSpeed]]**  |
| int32 | **[[HorizontalChangedDirectionCount]]**  |
| float | **[[HorizontalDirection]]**  |
| float | **[[HorizontalInitialDirection]]**  |
| float | **[[LeftTurnRateEndSpeed]]**  |
| float | **[[RightTurnRateEndSpeed]]**  |
| float | **[[SkippedFrameTime]]**  |
| float | **[[UpTurnRateEndSpeed]]**  |
| int32 | **[[VerticalChangedDirectionCount]]**  |
| float | **[[VerticalDirection]]**  |
| float | **[[VerticalInitialDirection]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200