package com.therapySessions.therapySessions.controller.response;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import java.util.Map;

@Data
//@AllArgsConstructor
@NoArgsConstructor
public class TherapyResponse {
    private String personalizedTherapyDetails;

    public TherapyResponse(String details) {
        this.personalizedTherapyDetails = details;
    }
}
