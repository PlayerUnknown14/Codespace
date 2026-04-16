using System.Drawing;

namespace Lab5_Variant5
{
    public class FormResult : Form
    {
        private Label labelResult;
        private Button buttonClose;

        public FormResult(string text)
        {
            this.Text = "Результат";
            this.Size = new Size(300, 200);
            this.StartPosition = FormStartPosition.CenterParent;
            this.FormBorderStyle = FormBorderStyle.FixedDialog;

            labelResult = new Label() 
            { 
                Text = text, 
                Location = new Point(10, 10), 
                Size = new Size(260, 100),
                AutoSize = false
            };

            buttonClose = new Button() 
            { 
                Text = "Закрыть", 
                Location = new Point(100, 120), 
                Size = new Size(80, 30) 
            };
            buttonClose.Click += (s, e) => this.Close();

            this.Controls.Add(labelResult);
            this.Controls.Add(buttonClose);
        }
    }
}