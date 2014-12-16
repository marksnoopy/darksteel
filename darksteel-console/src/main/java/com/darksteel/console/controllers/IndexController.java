package com.darksteel.console.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class IndexController {

    @RequestMapping("/index.do")
    public String index(Model model) {
        model.addAttribute("message", "Hello World!");  
        
        return "index2";
    }
}