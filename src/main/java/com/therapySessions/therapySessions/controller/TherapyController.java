package com.therapySessions.therapySessions.controller;

import com.therapySessions.therapySessions.controller.request.TherapyRequest;
import com.therapySessions.therapySessions.controller.response.TherapyResponse;
import com.therapySessions.therapySessions.service.PythonModelService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/therapy")
public class TherapyController {
    @Autowired
    private PythonModelService pythonModelService;

    @PostMapping("/recommend")
    public ResponseEntity<TherapyResponse> getRecommendation(@RequestBody TherapyRequest request) {
        TherapyResponse recommendation = pythonModelService.predictTherapy(
                request.getAge(),
                request.getGender(),
                request.getStressLevel()
        );
        return ResponseEntity.ok(recommendation);
    }

}
