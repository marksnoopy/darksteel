package com.darksteel.console.dao;

import java.util.List;

import com.darksteel.console.model.Task;

public interface TaskMapper {

    /**
     * 返回所有的数据
     * 
     * @return
     */
    public List<Task> getAll();
}
