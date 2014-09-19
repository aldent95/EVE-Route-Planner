package mapper;

import java.awt.BorderLayout;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JComponent;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JSlider;
import javax.swing.JTextArea;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.JToolBar;
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JMenuItem;
import javax.swing.JTextField;
import javax.swing.AbstractAction;
import javax.swing.Action;
import javax.swing.JComboBox;

public class GUI {
	private Mapper m;
	// GUI Fields
	private JFrame frame;
	private JTextArea textArea;
	private JComboBox start;
	private JComboBox end;

	public GUI(Mapper m) {
		this.m = m;
		setupFrame();
	}

	private void setupFrame() {
		frame = new JFrame("Graphics Example");
		frame.setSize(900, 900);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		JMenuBar menuBar = new JMenuBar();
		frame.setJMenuBar(menuBar);

		JMenu mnSettings = new JMenu("Settings");
		menuBar.add(mnSettings);

		JMenuItem mntmSettingsMenu = new JMenuItem("Settings Menu");
		mnSettings.add(mntmSettingsMenu);
		frame.getContentPane().setLayout(new BorderLayout(0, 0));

		JPanel panel = new JPanel();
		frame.getContentPane().add(panel, BorderLayout.NORTH);

		JLabel lblStart = new JLabel("Start");
		panel.add(lblStart);

		start = new JComboBox();
		start.setEditable(true);
		panel.add(start);

		JLabel lblEnd = new JLabel("End");
		panel.add(lblEnd);

		end = new JComboBox();
		end.setEditable(true);
		panel.add(end);

		JButton btnFindRoute = new JButton("Find Route");
		btnFindRoute.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				String s = (String) start.getSelectedItem();
				String e = (String) end.getSelectedItem();
				m.route(s, e);
			}
		});

		panel.add(btnFindRoute);

		textArea = new JTextArea();
		frame.getContentPane().add(textArea, BorderLayout.CENTER);
		frame.setVisible(true);
	}

	public void appendText(String text) {
		textArea.append(text);
	}

	public void clear() {
		textArea.setText("");
	}
}
