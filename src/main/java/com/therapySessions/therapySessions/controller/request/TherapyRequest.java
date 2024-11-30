package com.therapySessions.therapySessions.controller.request;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class TherapyRequest {
    private Integer age;
    private String gender;
    private Integer stressLevel;
}
