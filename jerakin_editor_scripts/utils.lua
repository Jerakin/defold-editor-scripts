local M = {}

function M.starts_with(str, start)
	return str:sub(1, #start) == start
end

function M.ends_with(str, ending)
	return ending == "" or str:sub(-#ending) == ending
end

function M.pack(...)
	return { ... }, select("#", ...) 
end 

function M.unpack(t, i)
	i = i or 1
	if t[i] ~= nil then
		return t[i], unpack(t, i + 1)
	end
end

return M