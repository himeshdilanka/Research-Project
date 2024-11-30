package com.therapySessions.therapySessions.service;

import com.therapySessions.therapySessions.controller.response.TherapyResponse;
import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;

@Service
public class PythonModelService {
    public TherapyResponse predictTherapy(int age, String gender, int stressLevel) {
        try {
            ProcessBuilder processBuilder = new ProcessBuilder(
                    "/Users/himeshdilankananayakkara/therapyenv/bin/python3",
                    "/Users/himeshdilankananayakkara/Desktop/Y4S1/reseach/my sample project/therapySessions/personalized_therapy.py"
            );
            processBuilder.redirectErrorStream(true);
            Process process = processBuilder.start();

            try (PrintWriter writer = new PrintWriter(
                    new OutputStreamWriter(process.getOutputStream(), StandardCharsets.UTF_8),
                    true
            )) {
                writer.println(age);
                writer.println(gender);
                writer.println(stressLevel);
            }

            StringBuilder output = new StringBuilder();
            try (BufferedReader reader = new BufferedReader(
                    new InputStreamReader(process.getInputStream(), StandardCharsets.UTF_8)
            )) {
                String line;
                while ((line = reader.readLine()) != null) {
                    output.append(line).append("\n");
                }
            }

            process.waitFor();
            return new TherapyResponse(output.toString().trim());
        } catch (Exception e) {
            return new TherapyResponse("Execution Error: " + e.getMessage());
        }
    }
}

//@Service
//public class PythonModelService {
//    public TherapyResponse predictTherapy(int age, String gender, int stressLevel) {
//
//        try {
//            ProcessBuilder processBuilder = new ProcessBuilder(
//                    "python3",
//                    "/Users/himeshdilankananayakkara/Desktop/Y4S1/reseach/my sample project/therapySessions/personalized_therapy.py"
//            );
//
//            processBuilder.redirectErrorStream(true);
//            Process process = processBuilder.start();
//
//            // Send inputs
//            try (PrintWriter writer = new PrintWriter(
//                    new OutputStreamWriter(process.getOutputStream(), StandardCharsets.UTF_8),
//                    true
//            )) {
//                writer.println(age);
//                writer.println(gender);
//                writer.println(stressLevel);
//            }
//
//            // Capture full output
//            StringBuilder output = new StringBuilder();
//            try (BufferedReader reader = new BufferedReader(
//                    new InputStreamReader(process.getInputStream(), StandardCharsets.UTF_8)
//            )) {
//                String line;
//                while ((line = reader.readLine()) != null) {
//                    output.append(line).append("\n");
//                }
//            }
//
//            // Wait for process to complete
//            process.waitFor();
//
//            return new TherapyResponse(output.toString().trim());
//        } catch (Exception e) {
//            e.printStackTrace();
//            return new TherapyResponse("Error in generating therapy recommendation");
//        }
//    }
//}
