# 可复用组件

## schemas

### `Array_Union_float__NoneType__Bits64_`

```json
{
  "items": {
    "anyOf": [
      {
        "type": "number"
      },
      {
        "type": "null"
      }
    ]
  },
  "type": "array",
  "title": "ArrayNullableFloatBits64"
}
```

### `CreateWebhookSubscriptionRequest`

```json
{
  "properties": {
    "callback_url": {
      "type": "string",
      "title": "Callback Url"
    },
    "verification_token": {
      "type": "string",
      "title": "Verification Token"
    },
    "event_type": {
      "$ref": "#/components/schemas/WebhookOperation"
    },
    "data_type": {
      "$ref": "#/components/schemas/ExtApiV2DataType"
    }
  },
  "type": "object",
  "required": [
    "callback_url",
    "verification_token",
    "event_type",
    "data_type"
  ],
  "title": "CreateWebhookSubscriptionRequest"
}
```

### `DailyResilienceModel`

```json
{
  "properties": {
    "id": {
      "type": "string",
      "title": "Id"
    },
    "day": {
      "type": "string",
      "format": "date",
      "title": "Day",
      "description": "Day when the resilience record was recorded."
    },
    "contributors": {
      "$ref": "#/components/schemas/ResilienceContributors",
      "description": "Contributors to the resilience score."
    },
    "level": {
      "$ref": "#/components/schemas/LongTermResilienceLevel",
      "description": "Resilience level."
    }
  },
  "type": "object",
  "required": [
    "id",
    "day",
    "contributors",
    "level"
  ],
  "title": "DailyResilienceModel"
}
```

### `EnhancedTagModel`

```json
{
  "properties": {
    "id": {
      "type": "string",
      "title": "Id"
    },
    "tag_type_code": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Tag Type Code",
      "description": "The unique code of the selected tag type, `NULL` for text-only tags, or `custom` for custom tag types."
    },
    "start_time": {
      "$ref": "#/components/schemas/LocalDateTime",
      "description": "Timestamp of the tag (if no duration) or the start time of the tag (with duration)."
    },
    "end_time": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/LocalDateTime"
        },
        {
          "type": "null"
        }
      ],
      "description": "Timestamp of the tag's end for events with duration or `NULL` if there is no duration."
    },
    "start_day": {
      "type": "string",
      "format": "date",
      "title": "Start Day",
      "description": "Day of the tag (if no duration) or the start day of the tag (with duration)."
    },
    "end_day": {
      "anyOf": [
        {
          "type": "string",
          "format": "date"
        },
        {
          "type": "null"
        }
      ],
      "title": "End Day",
      "description": "Day of the tag's end for events with duration or `NULL` if there is no duration."
    },
    "comment": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Comment",
      "description": "Additional freeform text on the tag."
    },
    "custom_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Custom Name",
      "description": "The name of the tag if the tag_type_code is `custom`."
    }
  },
  "type": "object",
  "required": [
    "id",
    "start_time",
    "start_day"
  ],
  "title": "EnhancedTagModel",
  "description": "An EnhancedTagModel maps an ASSATag. An ASSATag in ExtAPIV2 is called a EnhancedTag\nAn EnhancedTagModel will be populated by data from an ASSATag\nThe fields in the EnhancedTagModel map to fields in an ASSATag"
}
```

### `ExtApiV2DataType`

```json
{
  "type": "string",
  "enum": [
    "tag",
    "enhanced_tag",
    "workout",
    "session",
    "sleep",
    "daily_sleep",
    "daily_readiness",
    "daily_activity",
    "daily_spo2",
    "sleep_time",
    "rest_mode_period",
    "ring_configuration",
    "daily_stress",
    "daily_cardiovascular_age",
    "daily_resilience",
    "vo2_max"
  ],
  "title": "ExtApiV2DataType",
  "description": "Data types that partners can subscribe to via ExtApiV2 webhooks."
}
```

### `HTTPValidationError`

```json
{
  "properties": {
    "detail": {
      "items": {
        "$ref": "#/components/schemas/ValidationError"
      },
      "type": "array",
      "title": "Detail"
    }
  },
  "type": "object",
  "title": "HTTPValidationError"
}
```

### `ISODate`

```json
{
  "type": "string"
}
```

### `LocalDateTime`

```json
{
  "type": "string"
}
```

### `LocalizedDateTime`

```json
{
  "type": "string"
}
```

### `LongTermResilienceLevel`

```json
{
  "type": "string",
  "enum": [
    "limited",
    "adequate",
    "solid",
    "strong",
    "exceptional"
  ],
  "title": "LongTermResilienceLevel",
  "description": "Possible long term resilience level values."
}
```

### `MultiDocumentResponseDict`

```json
{
  "properties": {
    "data": {
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "type": "array",
      "title": "Data"
    },
    "next_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Next Token"
    }
  },
  "type": "object",
  "required": [
    "data",
    "next_token"
  ],
  "title": "MultiDocumentResponseDict"
}
```

### `MultiDocumentResponse_DailyResilienceModel_`

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/DailyResilienceModel"
      },
      "type": "array",
      "title": "Data"
    },
    "next_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Next Token"
    }
  },
  "type": "object",
  "required": [
    "data",
    "next_token"
  ],
  "title": "MultiDocumentResponse[DailyResilienceModel]"
}
```

### `MultiDocumentResponse_EnhancedTagModel_`

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/EnhancedTagModel"
      },
      "type": "array",
      "title": "Data"
    },
    "next_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Next Token"
    }
  },
  "type": "object",
  "required": [
    "data",
    "next_token"
  ],
  "title": "MultiDocumentResponse[EnhancedTagModel]"
}
```

### `MultiDocumentResponse_PublicDailyActivity_`

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/PublicDailyActivity"
      },
      "type": "array",
      "title": "Data"
    },
    "next_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Next Token"
    }
  },
  "type": "object",
  "required": [
    "data",
    "next_token"
  ],
  "title": "MultiDocumentResponse[PublicDailyActivity]"
}
```

### `MultiDocumentResponse_PublicDailyCardiovascularAge_`

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/PublicDailyCardiovascularAge"
      },
      "type": "array",
      "title": "Data"
    },
    "next_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Next Token"
    }
  },
  "type": "object",
  "required": [
    "data",
    "next_token"
  ],
  "title": "MultiDocumentResponse[PublicDailyCardiovascularAge]"
}
```

### `MultiDocumentResponse_PublicDailyReadiness_`

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/PublicDailyReadiness"
      },
      "type": "array",
      "title": "Data"
    },
    "next_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Next Token"
    }
  },
  "type": "object",
  "required": [
    "data",
    "next_token"
  ],
  "title": "MultiDocumentResponse[PublicDailyReadiness]"
}
```

### `MultiDocumentResponse_PublicDailySleep_`

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/PublicDailySleep"
      },
      "type": "array",
      "title": "Data"
    },
    "next_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Next Token"
    }
  },
  "type": "object",
  "required": [
    "data",
    "next_token"
  ],
  "title": "MultiDocumentResponse[PublicDailySleep]"
}
```

### `MultiDocumentResponse_PublicDailySpO2_`

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/PublicDailySpO2"
      },
      "type": "array",
      "title": "Data"
    },
    "next_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Next Token"
    }
  },
  "type": "object",
  "required": [
    "data",
    "next_token"
  ],
  "title": "MultiDocumentResponse[PublicDailySpO2]"
}
```

### `MultiDocumentResponse_PublicDailyStress_`

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/PublicDailyStress"
      },
      "type": "array",
      "title": "Data"
    },
    "next_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Next Token"
    }
  },
  "type": "object",
  "required": [
    "data",
    "next_token"
  ],
  "title": "MultiDocumentResponse[PublicDailyStress]"
}
```

### `MultiDocumentResponse_PublicModifiedSleepModel_`

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/PublicModifiedSleepModel"
      },
      "type": "array",
      "title": "Data"
    },
    "next_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Next Token"
    }
  },
  "type": "object",
  "required": [
    "data",
    "next_token"
  ],
  "title": "MultiDocumentResponse[PublicModifiedSleepModel]"
}
```

### `MultiDocumentResponse_PublicRestModePeriod_`

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/PublicRestModePeriod"
      },
      "type": "array",
      "title": "Data"
    },
    "next_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Next Token"
    }
  },
  "type": "object",
  "required": [
    "data",
    "next_token"
  ],
  "title": "MultiDocumentResponse[PublicRestModePeriod]"
}
```

### `MultiDocumentResponse_PublicRingConfiguration_`

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/PublicRingConfiguration"
      },
      "type": "array",
      "title": "Data"
    },
    "next_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Next Token"
    }
  },
  "type": "object",
  "required": [
    "data",
    "next_token"
  ],
  "title": "MultiDocumentResponse[PublicRingConfiguration]"
}
```

### `MultiDocumentResponse_PublicSession_`

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/PublicSession"
      },
      "type": "array",
      "title": "Data"
    },
    "next_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Next Token"
    }
  },
  "type": "object",
  "required": [
    "data",
    "next_token"
  ],
  "title": "MultiDocumentResponse[PublicSession]"
}
```

### `MultiDocumentResponse_PublicSleepTime_`

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/PublicSleepTime"
      },
      "type": "array",
      "title": "Data"
    },
    "next_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Next Token"
    }
  },
  "type": "object",
  "required": [
    "data",
    "next_token"
  ],
  "title": "MultiDocumentResponse[PublicSleepTime]"
}
```

### `MultiDocumentResponse_PublicVO2Max_`

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/PublicVO2Max"
      },
      "type": "array",
      "title": "Data"
    },
    "next_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Next Token"
    }
  },
  "type": "object",
  "required": [
    "data",
    "next_token"
  ],
  "title": "MultiDocumentResponse[PublicVO2Max]"
}
```

### `MultiDocumentResponse_PublicWorkout_`

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/PublicWorkout"
      },
      "type": "array",
      "title": "Data"
    },
    "next_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Next Token"
    }
  },
  "type": "object",
  "required": [
    "data",
    "next_token"
  ],
  "title": "MultiDocumentResponse[PublicWorkout]"
}
```

### `MultiDocumentResponse_TagModel_`

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/TagModel"
      },
      "type": "array",
      "title": "Data"
    },
    "next_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Next Token"
    }
  },
  "type": "object",
  "required": [
    "data",
    "next_token"
  ],
  "title": "MultiDocumentResponse[TagModel]"
}
```

### `PersonalInfoResponse`

```json
{
  "properties": {
    "id": {
      "type": "string",
      "title": "Id"
    },
    "age": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "Age"
    },
    "weight": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "title": "Weight"
    },
    "height": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "title": "Height"
    },
    "biological_sex": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Biological Sex"
    },
    "email": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Email"
    }
  },
  "type": "object",
  "required": [
    "id"
  ],
  "title": "PersonalInfoResponse"
}
```

### `PublicActivityContributors`

```json
{
  "properties": {
    "meet_daily_targets": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of meeting previous 7-day daily activity targets in range [1, 100]."
    },
    "move_every_hour": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of previous 24-hour inactivity alerts in range [1, 100]."
    },
    "recovery_time": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of previous 7-day recovery time in range [1, 100]."
    },
    "stay_active": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of previous 24-hour activity in range [1, 100]."
    },
    "training_frequency": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of previous 7-day exercise frequency in range [1, 100]."
    },
    "training_volume": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of previous 7-day exercise volume in range [1, 100]."
    }
  },
  "type": "object",
  "title": "PublicActivityContributors",
  "description": "Object defining activity score contributors."
}
```

### `PublicDailyActivity`

```json
{
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1,
      "title": "",
      "description": "Unique identifier of the object."
    },
    "active_calories": {
      "type": "integer",
      "title": "",
      "description": "Active calories expended in kilocalories."
    },
    "average_met_minutes": {
      "type": "number",
      "title": "",
      "description": "Average MET minutes."
    },
    "class_5_min": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "5-minute activity classification for the period where every character corresponds to:\n'0' = non wear\n'1' = rest\n'2' = inactive\n'3' = low activity\n'4' = medium activity\n'5' = high activity\nExample: \"001233334555524001\"."
    },
    "contributors": {
      "$ref": "#/components/schemas/PublicActivityContributors",
      "title": "",
      "description": "Object containing activity score contributors."
    },
    "day": {
      "$ref": "#/components/schemas/ISODate",
      "title": "",
      "description": "Day that the daily activity belong to."
    },
    "equivalent_walking_distance": {
      "type": "integer",
      "title": "",
      "description": "Equivalent walking distance of energe expenditure in meters."
    },
    "high_activity_met_minutes": {
      "type": "integer",
      "title": "",
      "description": "The total METs of each minute classified as high activity."
    },
    "high_activity_time": {
      "type": "integer",
      "title": "",
      "description": "The total time in seconds of each minute classified as high activity."
    },
    "inactivity_alerts": {
      "type": "integer",
      "title": "",
      "description": "Number of inactivity alerts received."
    },
    "low_activity_met_minutes": {
      "type": "integer",
      "title": "",
      "description": "The total METs of each minute classified as low activity."
    },
    "low_activity_time": {
      "type": "integer",
      "title": "",
      "description": "The total time in seconds of each minute classified as low activity."
    },
    "medium_activity_met_minutes": {
      "type": "integer",
      "title": "",
      "description": "The total METs of each minute classified as medium activity."
    },
    "medium_activity_time": {
      "type": "integer",
      "title": "",
      "description": "The total time in seconds of each minute classified as medium activity."
    },
    "met": {
      "$ref": "#/components/schemas/PublicSample",
      "title": "",
      "description": "Sample containing METs."
    },
    "meters_to_target": {
      "type": "integer",
      "title": "",
      "description": "Meters remaining to target."
    },
    "non_wear_time": {
      "type": "integer",
      "title": "",
      "description": "Ring non-wear time in seconds."
    },
    "resting_time": {
      "type": "integer",
      "title": "",
      "description": "Resting time in seconds."
    },
    "score": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Activity score in range [1, 100]."
    },
    "sedentary_met_minutes": {
      "type": "integer",
      "title": "",
      "description": "Sedentary MET minutes."
    },
    "sedentary_time": {
      "type": "integer",
      "title": "",
      "description": "Sedentary time in seconds."
    },
    "steps": {
      "type": "integer",
      "title": "",
      "description": "Total number of steps taken."
    },
    "target_calories": {
      "type": "integer",
      "title": "",
      "description": "Daily activity target in kilocalories."
    },
    "target_meters": {
      "type": "integer",
      "title": "",
      "description": "Daily activity target in meters."
    },
    "timestamp": {
      "$ref": "#/components/schemas/LocalizedDateTime",
      "title": "",
      "description": "Timestamp of the daily activity."
    },
    "total_calories": {
      "type": "integer",
      "title": "",
      "description": "Total calories expended in kilocalories."
    }
  },
  "type": "object",
  "required": [
    "id",
    "active_calories",
    "average_met_minutes",
    "contributors",
    "day",
    "equivalent_walking_distance",
    "high_activity_met_minutes",
    "high_activity_time",
    "inactivity_alerts",
    "low_activity_met_minutes",
    "low_activity_time",
    "medium_activity_met_minutes",
    "medium_activity_time",
    "met",
    "meters_to_target",
    "non_wear_time",
    "resting_time",
    "sedentary_met_minutes",
    "sedentary_time",
    "steps",
    "target_calories",
    "target_meters",
    "timestamp",
    "total_calories"
  ],
  "title": "PublicDailyActivity",
  "description": "Object defining a daily activity that is a 24-hour period starting at 4 a.m.",
  "x-cloud-only": true,
  "x-collection": "publicdailyactivity",
  "x-owner": "movement-squad"
}
```

### `PublicDailyCardiovascularAge`

```json
{
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1,
      "title": "",
      "description": "Unique identifier of the object."
    },
    "day": {
      "$ref": "#/components/schemas/ISODate",
      "title": "",
      "description": "Day that the prediction belongs to."
    },
    "pulse_wave_velocity": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Pulse wave velocity (m/s), derived from vascular age, with possible offset added."
    },
    "vascular_age": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Predicted vascular age in range [18, 100]."
    }
  },
  "type": "object",
  "required": [
    "id",
    "day"
  ],
  "title": "PublicDailyCardiovascularAge",
  "description": "Daily Cardiovascular Age.",
  "x-cloud-only": true,
  "x-collection": "publicdailycardiovascularage",
  "x-owner": "heart-health-squad"
}
```

### `PublicDailyReadiness`

```json
{
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1,
      "title": "",
      "description": "Unique identifier of the object."
    },
    "contributors": {
      "$ref": "#/components/schemas/PublicReadinessContributors",
      "title": "",
      "description": "Contributors of the daily readiness score."
    },
    "day": {
      "$ref": "#/components/schemas/ISODate",
      "title": "",
      "description": "Day that the daily readiness belongs to."
    },
    "score": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Daily readiness score."
    },
    "temperature_deviation": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Temperature deviation in degrees Celsius."
    },
    "temperature_trend_deviation": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Temperature trend deviation in degrees Celsius."
    },
    "timestamp": {
      "$ref": "#/components/schemas/LocalizedDateTime",
      "title": "",
      "description": "Timestamp of the daily readiness."
    }
  },
  "type": "object",
  "required": [
    "id",
    "contributors",
    "day",
    "timestamp"
  ],
  "title": "PublicDailyReadiness",
  "description": "Public object defining daily readiness.",
  "x-cloud-only": true,
  "x-collection": "publicdailyreadiness",
  "x-owner": "wellbeing-squad"
}
```

### `PublicDailySleep`

```json
{
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1,
      "title": "",
      "description": "Unique identifier of the object."
    },
    "contributors": {
      "$ref": "#/components/schemas/PublicSleepContributors",
      "title": "",
      "description": "Contributors for the daily sleep score."
    },
    "day": {
      "$ref": "#/components/schemas/ISODate",
      "title": "",
      "description": "Day that the daily sleep belongs to."
    },
    "score": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Daily sleep score."
    },
    "timestamp": {
      "$ref": "#/components/schemas/LocalizedDateTime",
      "title": "",
      "description": "Timestamp of the daily sleep."
    }
  },
  "type": "object",
  "required": [
    "id",
    "contributors",
    "day",
    "timestamp"
  ],
  "title": "PublicDailySleep",
  "description": "Public object defining daily sleep.",
  "x-cloud-only": true,
  "x-collection": "publicdailysleep",
  "x-owner": "sleep-squad"
}
```

### `PublicDailySpO2`

```json
{
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1,
      "title": "",
      "description": "Unique identifier of the object."
    },
    "breathing_disturbance_index": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Breathing Disturbance Index (BDI) calculated using detected SpO2 drops from timeseries. Values should be in range [0, 100]"
    },
    "day": {
      "$ref": "#/components/schemas/ISODate",
      "title": "",
      "description": "Day that the spo2 values belong to."
    },
    "spo2_percentage": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/PublicSpo2AggregatedValues"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "The daily SpO2 percentage value aggregates. Sourced from SpO2 percentage timeseries values."
    }
  },
  "type": "object",
  "required": [
    "id",
    "day"
  ],
  "title": "PublicDailySpO2",
  "description": "Daily SpO2 (Oxygen saturation).",
  "x-cloud-only": true,
  "x-collection": "publicdailyspo2",
  "x-owner": "sleep-squad"
}
```

### `PublicDailyStress`

```json
{
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1,
      "title": "",
      "description": "Unique identifier of the object."
    },
    "day": {
      "$ref": "#/components/schemas/ISODate",
      "title": "",
      "description": "Day that the daily stress belongs to."
    },
    "day_summary": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/PublicDailyStressSummary"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Stress summary of full day."
    },
    "recovery_high": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Time spent in a high recovery zone (bottom quartile data) in seconds."
    },
    "stress_high": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Time spent in a high stress zone (top quartile of data) in seconds."
    }
  },
  "type": "object",
  "required": [
    "id",
    "day"
  ],
  "title": "PublicDailyStress",
  "description": "Daily stress.",
  "x-cloud-only": true,
  "x-collection": "publicdailystress",
  "x-owner": "wellbeing-squad"
}
```

### `PublicDailyStressSummary`

```json
{
  "type": "string",
  "enum": [
    "restored",
    "normal",
    "stressful"
  ],
  "title": "PublicDailyStressSummary",
  "description": "Possible public daily stress summary types."
}
```

### `PublicHeartRateRow`

```json
{
  "properties": {
    "timestamp": {
      "$ref": "#/components/schemas/UtcDateTime",
      "title": "",
      "description": "Timestamp of the discrete sample."
    },
    "timestamp_unix": {
      "type": "integer",
      "title": "",
      "description": "Timestamp of the discrete sample as unix time in milliseconds."
    },
    "bpm": {
      "type": "integer",
      "title": "",
      "description": "Heart rate as beats per minute."
    },
    "source": {
      "$ref": "#/components/schemas/PublicHeartRateSource",
      "title": "",
      "description": "Source of the sample."
    }
  },
  "type": "object",
  "required": [
    "timestamp",
    "timestamp_unix",
    "bpm",
    "source"
  ],
  "title": "PublicHeartRateRow",
  "description": "Heart rate sample",
  "x-cloud-only": true,
  "x-collection": "publicheartrate",
  "x-owner": "core-sensing-squad"
}
```

### `PublicHeartRateSource`

```json
{
  "type": "string",
  "enum": [
    "awake",
    "workout",
    "rest",
    "sleep",
    "live",
    "session"
  ],
  "title": "PublicHeartRateSource",
  "description": "Possible heart rate sources."
}
```

### `PublicModifiedSleepModel`

```json
{
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1,
      "title": "",
      "description": "Unique identifier of the object."
    },
    "average_breath": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Average breathing rate during sleep as breaths/minute."
    },
    "average_heart_rate": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Average heart rate during sleep as beats/minute. NOTE: this is the average calculated by ecore (based on 30-second samples) which is different from what is shown in the app. The app shows the average of aggregated 5-minute heart rate samples."
    },
    "average_hrv": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Average heart rate variability during sleep."
    },
    "awake_time": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Duration spent awake in seconds."
    },
    "bedtime_end": {
      "$ref": "#/components/schemas/LocalizedDateTime",
      "title": "",
      "description": "Bedtime end of the sleep."
    },
    "bedtime_start": {
      "$ref": "#/components/schemas/LocalizedDateTime",
      "title": "",
      "description": "Bedtime start of the sleep."
    },
    "day": {
      "$ref": "#/components/schemas/ISODate",
      "title": "",
      "description": "Day that the sleep belongs to."
    },
    "deep_sleep_duration": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Duration spent in deep sleep in seconds."
    },
    "efficiency": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Sleep efficiency rating in range [1, 100]."
    },
    "heart_rate": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/PublicSample"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Object containing heart rate samples."
    },
    "hrv": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/PublicSample"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Object containing heart rate variability samples."
    },
    "latency": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Sleep latency in seconds. This is the time it took for the user to fall asleep after going to bed."
    },
    "light_sleep_duration": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Duration spent in light sleep in seconds."
    },
    "low_battery_alert": {
      "type": "boolean",
      "title": "",
      "description": "Flag indicating if a low battery alert occurred."
    },
    "lowest_heart_rate": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Lowest heart rate during sleep. NOTE: this is the value calculated by ecore (based on 30-second samples) which is different from what is shown in the app. The app shows the minimum of aggregated 5-minute heart rate samples."
    },
    "movement_30_sec": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "30-second movement classification for the period where every character corresponds to:\n'1' = no motion,\n'2' = restless,\n'3' = tossing and turning\n'4' = active\nExample: \"1143222134\"."
    },
    "period": {
      "type": "integer",
      "title": "",
      "description": "ECore sleep period identifier."
    },
    "readiness": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/PublicReadiness"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Object containing the readiness details."
    },
    "readiness_score_delta": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Effect on readiness score caused by this sleep period."
    },
    "rem_sleep_duration": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Duration spent in REM sleep in seconds."
    },
    "restless_periods": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Number of restless periods during sleep."
    },
    "sleep_algorithm_version": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/PublicSleepAlgorithmVersion"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Version of the sleep algorithm used to calculate the sleep data."
    },
    "sleep_analysis_reason": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/PublicSleepAnalysisReason"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "The reason for the creation or update of the latest version of this sleep."
    },
    "sleep_phase_30_sec": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "30-second sleep phase classification for the period where every character corresponds to:\n'1' = deep sleep,\n'2' = light sleep,\n'3' = REM sleep\n'4' = awake.\nExample: \"444423323441114\"."
    },
    "sleep_phase_5_min": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "5-minute sleep phase classification for the period where every character corresponds to:\n'1' = deep sleep,\n'2' = light sleep,\n'3' = REM sleep\n'4' = awake.\nExample: \"444423323441114\"."
    },
    "sleep_score_delta": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Effect on sleep score caused by this sleep period."
    },
    "time_in_bed": {
      "type": "integer",
      "title": "",
      "description": "Duration spent in bed in seconds."
    },
    "total_sleep_duration": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Total sleep duration in seconds."
    },
    "type": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/PublicSleepType"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Type of the sleep period."
    },
    "ring_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Ring Id",
      "description": "Encrypted identifier of the ring that produced this sleep data. Deprecated, returns null."
    },
    "app_sleep_phase_5_min": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "App Sleep Phase 5 Min",
      "description": "\n        5-minute sleep phase classification for the period aligned with what is shown in the app\n        where every character corresponds to:\n        '1' = deep sleep,\n        '2' = light sleep,\n        '3' = REM sleep\n        '4' = awake.\n        Example: \"444423323441114\".\n        NOTE: This field will be removed in the future after a transition period.\n        "
    }
  },
  "type": "object",
  "required": [
    "id",
    "bedtime_end",
    "bedtime_start",
    "day",
    "low_battery_alert",
    "period",
    "time_in_bed"
  ],
  "title": "PublicModifiedSleepModel",
  "x-cloud-only": true,
  "x-collection": "publicsleepmodel",
  "x-owner": "sleep-squad"
}
```

### `PublicMomentMood`

```json
{
  "type": "string",
  "enum": [
    "bad",
    "worse",
    "same",
    "good",
    "great"
  ],
  "title": "PublicMomentMood",
  "description": "Possible Moment moods."
}
```

### `PublicMomentType`

```json
{
  "type": "string",
  "enum": [
    "breathing",
    "meditation",
    "nap",
    "relaxation",
    "rest",
    "body_status"
  ],
  "title": "PublicMomentType",
  "description": "Possible Moment types."
}
```

### `PublicReadiness`

```json
{
  "properties": {
    "contributors": {
      "$ref": "#/components/schemas/PublicReadinessContributors",
      "title": "",
      "description": "Contributors of the readiness score."
    },
    "score": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Readiness score in range [1, 100]."
    },
    "temperature_deviation": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Temperature deviation in degrees Celsius."
    },
    "temperature_trend_deviation": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Temperature trend deviation in degrees Celsius."
    }
  },
  "type": "object",
  "required": [
    "contributors"
  ],
  "title": "PublicReadiness",
  "description": "Object defining readiness."
}
```

### `PublicReadinessContributors`

```json
{
  "properties": {
    "activity_balance": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of cumulative activity balance in range [1, 100]."
    },
    "body_temperature": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of body temperature in range [1, 100]."
    },
    "hrv_balance": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of heart rate variability balance in range [1, 100]."
    },
    "previous_day_activity": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of previous day's activity in range [1, 100]."
    },
    "previous_night": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of previous night's sleep in range [1, 100]."
    },
    "recovery_index": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of recovery index in range [1, 100]."
    },
    "resting_heart_rate": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of resting heart rate in range [1, 100]."
    },
    "sleep_balance": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of sleep balance in range [1, 100]."
    },
    "sleep_regularity": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of sleep regularity in range [1, 100]."
    }
  },
  "type": "object",
  "title": "PublicReadinessContributors",
  "description": "Object defining readiness score contributors."
}
```

### `PublicRestModeEpisode`

```json
{
  "properties": {
    "tags": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "title": "",
      "description": "Tags selected for the episode."
    },
    "timestamp": {
      "$ref": "#/components/schemas/LocalizedDateTime",
      "title": "",
      "description": "Timestamp indicating when the episode occurred."
    }
  },
  "type": "object",
  "required": [
    "tags",
    "timestamp"
  ],
  "title": "PublicRestModeEpisode",
  "description": "Object defining a public Rest Mode episode."
}
```

### `PublicRestModePeriod`

```json
{
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1,
      "title": "",
      "description": "Unique identifier of the object."
    },
    "end_day": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/ISODate"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "End date of rest mode."
    },
    "end_time": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/LocalizedDateTime"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Timestamp when rest mode ended."
    },
    "episodes": {
      "items": {
        "$ref": "#/components/schemas/PublicRestModeEpisode"
      },
      "type": "array",
      "title": "",
      "description": "Collection of episodes during rest mode, consisting of tags."
    },
    "start_day": {
      "$ref": "#/components/schemas/ISODate",
      "title": "",
      "description": "Start date of rest mode."
    },
    "start_time": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/LocalizedDateTime"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Timestamp when rest mode ended."
    }
  },
  "type": "object",
  "required": [
    "id",
    "episodes",
    "start_day"
  ],
  "title": "PublicRestModePeriod",
  "description": "Rest mode episode information.",
  "x-cloud-only": true,
  "x-collection": "publicrestmodeperiod",
  "x-owner": "sleep-squad"
}
```

### `PublicRingBatteryLevelRow`

```json
{
  "properties": {
    "timestamp": {
      "$ref": "#/components/schemas/UtcDateTime",
      "title": "",
      "description": "Timestamp of the discrete sample."
    },
    "timestamp_unix": {
      "type": "integer",
      "title": "",
      "description": "Timestamp of the discrete sample as unix time in milliseconds."
    },
    "charging": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Flag indicating if the ring was charging."
    },
    "in_charger": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Flag indicating if the ring was in charger."
    },
    "level": {
      "type": "integer",
      "title": "",
      "description": "Ring battery level percentage. These values are within [0, 100]."
    }
  },
  "type": "object",
  "required": [
    "timestamp",
    "timestamp_unix",
    "level"
  ],
  "title": "PublicRingBatteryLevelRow",
  "description": "Object defining a ring battery level event.",
  "x-cloud-only": true,
  "x-collection": "publicringbatterylevel",
  "x-owner": "connectivity-squad"
}
```

### `PublicRingColor`

```json
{
  "type": "string",
  "enum": [
    "brushed_silver",
    "glossy_black",
    "glossy_gold",
    "glossy_white",
    "gucci",
    "matt_gold",
    "rose",
    "silver",
    "stealth_black",
    "titanium",
    "titanium_and_gold",
    "cloud",
    "petal",
    "midnight",
    "tide",
    "deep_rose"
  ],
  "title": "PublicRingColor",
  "description": "Possible ring colors."
}
```

### `PublicRingConfiguration`

```json
{
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1,
      "title": "",
      "description": "Unique identifier of the object."
    },
    "color": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/PublicRingColor"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Color of the ring."
    },
    "design": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/PublicRingDesign"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Design of the ring."
    },
    "firmware_version": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Firmware version of the ring."
    },
    "hardware_type": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/PublicRingHardwareType"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Hardware type of the ring."
    },
    "set_up_at": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/UtcDateTime"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "UTC timestamp indicating when the ring was set up."
    },
    "size": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "US size of the ring."
    }
  },
  "type": "object",
  "required": [
    "id"
  ],
  "title": "PublicRingConfiguration",
  "description": "Ring configuration.",
  "x-cloud-only": true,
  "x-collection": "publicringconfiguration",
  "x-owner": "connectivity-squad"
}
```

### `PublicRingDesign`

```json
{
  "type": "string",
  "enum": [
    "heritage",
    "balance",
    "balance_diamond",
    "horizon",
    "ceramic"
  ],
  "title": "PublicRingDesign",
  "description": "Possible ring designs."
}
```

### `PublicRingHardwareType`

```json
{
  "type": "string",
  "enum": [
    "gen1",
    "gen2",
    "gen2m",
    "gen3",
    "gen4",
    "or5"
  ],
  "title": "PublicRingHardwareType",
  "description": "Possible ring hardware types."
}
```

### `PublicSample`

```json
{
  "properties": {
    "interval": {
      "type": "number",
      "title": "",
      "description": "Interval in seconds between the sampled items."
    },
    "items": {
      "$ref": "#/components/schemas/Array_Union_float__NoneType__Bits64_",
      "title": "",
      "description": "Recorded sample items."
    },
    "timestamp": {
      "$ref": "#/components/schemas/LocalizedDateTime",
      "title": "",
      "description": "Timestamp when the sample recording started."
    }
  },
  "type": "object",
  "required": [
    "interval",
    "items",
    "timestamp"
  ],
  "title": "PublicSample",
  "description": "Object defining a recorded sample."
}
```

### `PublicSession`

```json
{
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1,
      "title": "",
      "description": "Unique identifier of the object."
    },
    "day": {
      "$ref": "#/components/schemas/ISODate",
      "title": "",
      "description": "The date when the session occurred."
    },
    "end_datetime": {
      "$ref": "#/components/schemas/LocalizedDateTime",
      "title": "",
      "description": "Timestamp indicating when the Moment ended."
    },
    "heart_rate": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/PublicSample"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Recorded heart rate samples during the Moment."
    },
    "heart_rate_variability": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/PublicSample"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Recorded heart rate variability samples during the Moment."
    },
    "mood": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/PublicMomentMood"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "User-selected mood for the Moment."
    },
    "motion_count": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/PublicSample"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Recorded motion count samples during the Moment."
    },
    "start_datetime": {
      "$ref": "#/components/schemas/LocalizedDateTime",
      "title": "",
      "description": "Timestamp indicating when the Moment started."
    },
    "type": {
      "$ref": "#/components/schemas/PublicMomentType",
      "title": "",
      "description": "Type of the Moment."
    }
  },
  "type": "object",
  "required": [
    "id",
    "day",
    "end_datetime",
    "start_datetime",
    "type"
  ],
  "title": "PublicSession",
  "description": "Public model defining a recorded Session.",
  "x-cloud-only": true,
  "x-collection": "publicsession",
  "x-owner": "wellbeing-squad"
}
```

### `PublicSleepAlgorithmVersion`

```json
{
  "type": "string",
  "enum": [
    "v1",
    "v2"
  ],
  "title": "PublicSleepAlgorithmVersion",
  "description": "Oura Sleep Staging Algorithms.\nv1 = original aka legacy aka OSSA 1.0,\nv2 = latest sleep algorithm"
}
```

### `PublicSleepAnalysisReason`

```json
{
  "type": "string",
  "enum": [
    "foreground_sleep_analysis",
    "bedtime_edit",
    "background_sleep_analysis",
    "background_created_foreground_updated"
  ],
  "title": "PublicSleepAnalysisReason",
  "description": "Possible sleep analysis reasons."
}
```

### `PublicSleepContributors`

```json
{
  "properties": {
    "deep_sleep": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of deep sleep in range [1, 100]."
    },
    "efficiency": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of sleep efficiency in range [1, 100]."
    },
    "latency": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of sleep latency in range [1, 100]."
    },
    "rem_sleep": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of REM sleep in range [1, 100]."
    },
    "restfulness": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of sleep restfulness in range [1, 100]."
    },
    "timing": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of sleep timing in range [1, 100]."
    },
    "total_sleep": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Contribution of total sleep in range [1, 100]."
    }
  },
  "type": "object",
  "title": "PublicSleepContributors",
  "description": "Object defining sleep score contributors."
}
```

### `PublicSleepTime`

```json
{
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1,
      "title": "",
      "description": "Unique identifier of the object."
    },
    "day": {
      "$ref": "#/components/schemas/ISODate",
      "title": "",
      "description": "Corresponding day for the sleep time."
    },
    "optimal_bedtime": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/PublicSleepTimeWindow"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Optimal bedtime."
    },
    "recommendation": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/PublicSleepTimeRecommendation"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Recommended action for bedtime."
    },
    "status": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/PublicSleepTimeStatus"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Sleep time status; used to inform sleep time recommendation."
    }
  },
  "type": "object",
  "required": [
    "id",
    "day"
  ],
  "title": "PublicSleepTime",
  "description": "Suggested bedtime for the user.",
  "x-cloud-only": true,
  "x-collection": "publicsleeptime",
  "x-owner": "sleep-squad"
}
```

### `PublicSleepTimeRecommendation`

```json
{
  "type": "string",
  "enum": [
    "improve_efficiency",
    "earlier_bedtime",
    "later_bedtime",
    "earlier_wake_up_time",
    "later_wake_up_time",
    "follow_optimal_bedtime"
  ],
  "title": "PublicSleepTimeRecommendation",
  "description": "Possible public SleepTime recommendation."
}
```

### `PublicSleepTimeStatus`

```json
{
  "type": "string",
  "enum": [
    "not_enough_nights",
    "not_enough_recent_nights",
    "bad_sleep_quality",
    "only_recommended_found",
    "optimal_found"
  ],
  "title": "PublicSleepTimeStatus",
  "description": "Possible public SleepTime status."
}
```

### `PublicSleepTimeWindow`

```json
{
  "properties": {
    "day_tz": {
      "type": "integer",
      "title": "",
      "description": "Timezone offset in second from GMT of the day"
    },
    "end_offset": {
      "type": "integer",
      "title": "",
      "description": "End offset from midnight in second"
    },
    "start_offset": {
      "type": "integer",
      "title": "",
      "description": "Start offset from midnight in second"
    }
  },
  "type": "object",
  "required": [
    "day_tz",
    "end_offset",
    "start_offset"
  ],
  "title": "PublicSleepTimeWindow",
  "description": "Object defining sleep time window"
}
```

### `PublicSleepType`

```json
{
  "type": "string",
  "enum": [
    "deleted",
    "sleep",
    "long_sleep",
    "late_nap",
    "rest"
  ],
  "title": "PublicSleepType",
  "description": "Possible sleep period types.\n'deleted' = deleted sleep by user.\n'sleep' = user confirmed sleep / nap, min 15 minutes, max 3 hours, contributes to daily scores\n'late_nap' = user confirmed sleep / nap, min 15 minutes, ended after sleep day change (6 pm), contributes to next days daily scores\n'long_sleep' = sleep that is long enough (>3h) to automatically contribute to daily scores\n'rest' = Falsely detected sleep / nap, rejected in confirm prompt by user"
}
```

### `PublicSpo2AggregatedValues`

```json
{
  "properties": {
    "average": {
      "type": "number",
      "title": "",
      "description": "Average of spo2."
    }
  },
  "type": "object",
  "required": [
    "average"
  ],
  "title": "PublicSpo2AggregatedValues",
  "description": "Object defining public spo2 aggregated values."
}
```

### `PublicVO2Max`

```json
{
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1,
      "title": "",
      "description": "Unique identifier of the object."
    },
    "day": {
      "$ref": "#/components/schemas/ISODate",
      "title": "",
      "description": "Day that the estimate belongs to."
    },
    "timestamp": {
      "$ref": "#/components/schemas/LocalizedDateTime",
      "title": "",
      "description": "Timestamp indicating when the estimate was created."
    },
    "vo2_max": {
      "type": "integer",
      "title": "",
      "description": "VO2 max value."
    }
  },
  "type": "object",
  "required": [
    "id",
    "day",
    "timestamp",
    "vo2_max"
  ],
  "title": "PublicVO2Max",
  "description": "VO2Max estimate.",
  "x-cloud-only": true,
  "x-collection": "publicvo2max",
  "x-owner": "movement-squad"
}
```

### `PublicWorkout`

```json
{
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1,
      "title": "",
      "description": "Unique identifier of the object."
    },
    "activity": {
      "type": "string",
      "title": "",
      "description": "Type of the workout activity."
    },
    "calories": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Energy burned in kilocalories during the workout."
    },
    "day": {
      "$ref": "#/components/schemas/ISODate",
      "title": "",
      "description": "Day when the workout occurred."
    },
    "distance": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "Distance traveled in meters during the workout."
    },
    "end_datetime": {
      "$ref": "#/components/schemas/LocalizedDateTime",
      "title": "",
      "description": "Timestamp indicating when the workout ended."
    },
    "intensity": {
      "$ref": "#/components/schemas/PublicWorkoutIntensity",
      "title": "",
      "description": "Intensity of the workout."
    },
    "label": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "",
      "description": "User-defined label for the workout."
    },
    "source": {
      "$ref": "#/components/schemas/PublicWorkoutSource",
      "title": "",
      "description": "Possible workout sources."
    },
    "start_datetime": {
      "$ref": "#/components/schemas/LocalizedDateTime",
      "title": "",
      "description": "Timestamp indicating when the workout started."
    }
  },
  "type": "object",
  "required": [
    "id",
    "activity",
    "day",
    "end_datetime",
    "intensity",
    "source",
    "start_datetime"
  ],
  "title": "PublicWorkout",
  "description": "Public model for Workout.",
  "x-cloud-only": true,
  "x-collection": "publicworkout",
  "x-owner": "movement-squad"
}
```

### `PublicWorkoutIntensity`

```json
{
  "type": "string",
  "enum": [
    "easy",
    "moderate",
    "hard"
  ],
  "title": "PublicWorkoutIntensity",
  "description": "Possible workout intensities."
}
```

### `PublicWorkoutSource`

```json
{
  "type": "string",
  "enum": [
    "manual",
    "autodetected",
    "confirmed",
    "workout_heart_rate",
    "live_third_party_heart_rate",
    "live_oura_heart_rate"
  ],
  "title": "PublicWorkoutSource",
  "description": "Possible workout sources."
}
```

### `ResilienceContributors`

```json
{
  "properties": {
    "sleep_recovery": {
      "type": "number",
      "title": "Sleep Recovery",
      "description": "Sleep recovery contributor to the resilience score. Range: [0, 100]"
    },
    "daytime_recovery": {
      "type": "number",
      "title": "Daytime Recovery",
      "description": "Daytime recovery contributor to the resilience score. Range: [0, 100]"
    },
    "stress": {
      "type": "number",
      "title": "Stress",
      "description": "Stress contributor to the resilience score. Range: [0, 100]"
    }
  },
  "type": "object",
  "required": [
    "sleep_recovery",
    "daytime_recovery",
    "stress"
  ],
  "title": "ResilienceContributors"
}
```

### `TagModel`

```json
{
  "properties": {
    "id": {
      "type": "string",
      "title": "Id"
    },
    "day": {
      "type": "string",
      "format": "date",
      "title": "Day",
      "description": "Day that the note belongs to."
    },
    "text": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Text",
      "description": "Textual contents of the note."
    },
    "timestamp": {
      "$ref": "#/components/schemas/LocalDateTime",
      "description": "Timestamp of the note."
    },
    "tags": {
      "items": {
        "type": "string"
      },
      "type": "array",
      "title": "Tags",
      "description": "Selected tags for the tag."
    }
  },
  "type": "object",
  "required": [
    "id",
    "day",
    "text",
    "timestamp",
    "tags"
  ],
  "title": "TagModel",
  "description": "A TagModel maps to an ASSANote. An ASSANote in ExtAPIV2 is called a Tag\nA TagModel will be populated by data from an ASSANote\nThe fields in the TagModel map to fields in an ASSANote"
}
```

### `TimeSeriesResponseDict`

```json
{
  "properties": {
    "data": {
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "type": "array",
      "title": "Data"
    },
    "next_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Next Token"
    }
  },
  "type": "object",
  "required": [
    "data"
  ],
  "title": "TimeSeriesResponseDict"
}
```

### `TimeSeriesResponse_PublicHeartRateRow_`

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/PublicHeartRateRow"
      },
      "type": "array",
      "title": "Data"
    },
    "next_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Next Token"
    }
  },
  "type": "object",
  "required": [
    "data"
  ],
  "title": "TimeSeriesResponse[PublicHeartRateRow]"
}
```

### `TimeSeriesResponse_PublicRingBatteryLevelRow_`

```json
{
  "properties": {
    "data": {
      "items": {
        "$ref": "#/components/schemas/PublicRingBatteryLevelRow"
      },
      "type": "array",
      "title": "Data"
    },
    "next_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Next Token"
    }
  },
  "type": "object",
  "required": [
    "data"
  ],
  "title": "TimeSeriesResponse[PublicRingBatteryLevelRow]"
}
```

### `UpdateWebhookSubscriptionRequest`

```json
{
  "properties": {
    "verification_token": {
      "type": "string",
      "title": "Verification Token"
    },
    "callback_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "title": "Callback Url"
    },
    "event_type": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/WebhookOperation"
        },
        {
          "type": "null"
        }
      ]
    },
    "data_type": {
      "anyOf": [
        {
          "$ref": "#/components/schemas/ExtApiV2DataType"
        },
        {
          "type": "null"
        }
      ]
    }
  },
  "type": "object",
  "required": [
    "verification_token"
  ],
  "title": "UpdateWebhookSubscriptionRequest"
}
```

### `UtcDateTime`

```json
{
  "type": "string"
}
```

### `ValidationError`

```json
{
  "properties": {
    "loc": {
      "items": {
        "anyOf": [
          {
            "type": "string"
          },
          {
            "type": "integer"
          }
        ]
      },
      "type": "array",
      "title": "Location"
    },
    "msg": {
      "type": "string",
      "title": "Message"
    },
    "type": {
      "type": "string",
      "title": "Error Type"
    },
    "input": {
      "title": "Input"
    },
    "ctx": {
      "type": "object",
      "title": "Context"
    }
  },
  "type": "object",
  "required": [
    "loc",
    "msg",
    "type"
  ],
  "title": "ValidationError"
}
```

### `WebhookOperation`

```json
{
  "type": "string",
  "enum": [
    "create",
    "update",
    "delete"
  ],
  "title": "WebhookOperation"
}
```

### `WebhookSubscriptionModel`

```json
{
  "properties": {
    "id": {
      "type": "string",
      "format": "uuid4",
      "title": "Id"
    },
    "callback_url": {
      "type": "string",
      "title": "Callback Url"
    },
    "event_type": {
      "$ref": "#/components/schemas/WebhookOperation"
    },
    "data_type": {
      "$ref": "#/components/schemas/ExtApiV2DataType"
    },
    "expiration_time": {
      "type": "string",
      "format": "date-time",
      "title": "Expiration Time"
    }
  },
  "type": "object",
  "required": [
    "id",
    "callback_url",
    "event_type",
    "data_type",
    "expiration_time"
  ],
  "title": "WebhookSubscriptionModel"
}
```

## securitySchemes

### `BearerAuth`

```json
{
  "type": "http",
  "scheme": "bearer"
}
```

### `OAuth2`

```json
{
  "type": "oauth2",
  "flows": {
    "authorizationCode": {
      "authorizationUrl": "https://cloud.ouraring.com/oauth/authorize",
      "tokenUrl": "https://api.ouraring.com/oauth/token",
      "scopes": {
        "email": "Email address of the user",
        "personal": "Personal information (gender, age, height, weight)",
        "daily": "Daily summaries of sleep, activity and readiness",
        "heartrate": "Time series heart rate for users",
        "workout": "Summaries for auto-detected and user entered workouts",
        "tag": "User entered tags",
        "session": "Guided and unguided sessions in the Oura app",
        "spo2": "SpO2 Average recorded during sleep",
        "heart_health": "Heart health data"
      }
    }
  }
}
```

### `ClientIdAuth`

```json
{
  "type": "apiKey",
  "in": "header",
  "name": "x-client-id",
  "description": "Client ID for webhook subscription endpoints. Must be used together with x-client-secret header."
}
```

### `ClientSecretAuth`

```json
{
  "type": "apiKey",
  "in": "header",
  "name": "x-client-secret",
  "description": "Client Secret for webhook subscription endpoints. Must be used together with x-client-id header."
}
```
