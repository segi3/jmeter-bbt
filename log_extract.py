with open ('./logs/result_50k.csv', 'r') as f:
    logs = [log for log in f if "MQTT Sub Sampler" in log]

succeed = []
failed_empty_response = []
failed_late = []
failed_others = []

for l in logs:
    if "true" in l:
        succeed.append(l)
    elif "[Invalid server time response timestamps]" in l:
        failed_empty_response.append(l)
    elif "[Time difference exceeds 2 seconds]" in l:
        failed_late.append(l)
    else:
        failed_others.append(l)

print('Summary:\nSucceed: {}\nFailed empty response: {}\nFailed late arrival: {}\nFailed others: {}'.format(len(succeed), len(failed_empty_response), len(failed_late), len(failed_others)))