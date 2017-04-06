$(function(){ // on dom ready

var cy = cytoscape({
  container: document.getElementById('cy'),
  
  style: [
    {
      selector: 'node',
      css: {
        'content': 'data(id)',
        'text-valign': 'center',
        'text-halign': 'center'
      }
    },
    {
      selector: 'edge',
      css: {
        'target-arrow-shape': 'triangle'
      }
    },
    {
      selector: ':selected',
      css: {
        'background-color': 'red',
        'line-color': 'red',
        'target-arrow-color': 'red',
        'source-arrow-color': 'red'
      }
    }
  ],
  
  elements: {
    nodes: [
      { data: { id: 'thread_Root' } },
      { data: { id: 'bdsFastq', parent: 'thread_Root' } },
      { data: { id: 'bdsSort', parent: 'thread_Root' } },
      { data: { id: 'bdsIndex', parent: 'thread_Root' } },
      { data: { id: 'bdsAlign', parent: 'thread_Root' } },
    ],
    edges: [
      { data: { id: 'None-thread_Root', source: 'None', target: 'thread_Root' } },
      { data: { id: 'threadid-threadid', source: 'threadid', target: 'threadid' } },
      { data: { id: 'bdsAlign-bdsSort', source: 'bdsAlign', target: 'bdsSort' } },
      { data: { id: 'bdsAlign-bdsSort', source: 'bdsAlign', target: 'bdsSort' } },
      { data: { id: 'bdsSort-bdsIndex', source: 'bdsSort', target: 'bdsIndex' } },
      { data: { id: 'bdsSort-bdsIndex', source: 'bdsSort', target: 'bdsIndex' } },
      { data: { id: 'bdsFastq-bdsAlign', source: 'bdsFastq', target: 'bdsAlign' } },
      { data: { id: 'bdsFastq-bdsAlign', source: 'bdsFastq', target: 'bdsAlign' } },
      { data: { id: 'bdsFastq-bdsAlign', source: 'bdsFastq', target: 'bdsAlign' } },
      { data: { id: 'bdsFastq-bdsAlign', source: 'bdsFastq', target: 'bdsAlign' } },
      { data: { id: 'taskid-taskid', source: 'taskid', target: 'taskid' } },
    ]
  },
  
  layout: {
    name: 'breadthfirst',
  }
});

}); // on dom ready

