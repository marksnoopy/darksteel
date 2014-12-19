package com.darksteel.console.controllers;

import java.util.List;

import javax.annotation.Resource;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import com.darksteel.console.dao.TaskMapper;
import com.darksteel.console.model.Task;

@Controller
public class IndexController {

    @Resource
    TaskMapper taskDao;
    
    
    @RequestMapping("/index.do")
    public String index(Model model) {
        model.addAttribute("message", "Hello World!");  
        
        List<Task> taskList = taskDao.getAll();
        System.out.println(taskList.get(0).getTaskName());
        return "index2";
    }
}
