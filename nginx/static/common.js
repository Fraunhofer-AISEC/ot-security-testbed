const local = {
    hmi_url: "http://localhost:4001",
    hist_url: "http://localhost:4002",
    vis_url: "http://localhost:4003",
    plc_url: "http://localhost:4004",
    attacker_url: "http://localhost:4005",
    docs_url: "http://localhost:4000/docs"
}

const prod = {
    hmi_url: "https://hmi-plctb.aisec.fraunhofer.de",
    hist_url: "https://hist-plctb.aisec.fraunhofer.de",
    vis_url: "https://vis-plctb.aisec.fraunhofer.de",
    plc_url: "https://plc-plctb.aisec.fraunhofer.de",
    attacker_url: "https://attacker-plctb.aisec.fraunhofer.de",
    docs_url: "https://docs-plctb.aisec.fraunhofer.de"
}
const urls = (document.location.hostname === "localhost") ? local : prod;

document.querySelectorAll("a, iframe").forEach(elem => {
    console.log(elem);
    let att_key;
    if (elem.tagName === "A")
        att_key = "href";
    else if (elem.tagName === "IFRAME")
        att_key = "src";
    let template = elem.getAttribute(att_key);
    console.log(elem.tagName, template, att_key)
    for (const [key, value] of Object.entries(urls)) {
        template = template.replace(`{{${key}}}`, value);
    }
    elem.setAttribute(att_key, template);
})