fetch('mindmap_data.json')
  .then(response => response.json())
  .then(data => {
    var mind = {
      meta: { name: 'Fire Protection Standards', author: 'Casey Bladow', version: '1.0' },
      format: 'node_tree',
      data: data
    };
    var options = { container: 'jsmind_container', editable: false, theme: 'primary' };
    var jm = new jsMind(options);
    jm.show(mind);
  })
  .catch(error => console.error('Error loading mind map data:', error));